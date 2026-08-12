"""Application wiring: build the FastAPI app and attach everything to it."""

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import pages
from app.chat import router as chat_router
from app.settings import STATIC_URL

PACKAGE_DIR = Path(__file__).resolve().parent


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
    )
    app.mount(
        STATIC_URL,
        StaticFiles(directory=str(PACKAGE_DIR / "static")),
        name="static",
    )

    pages.templates = Jinja2Templates(directory=str(PACKAGE_DIR / "templates"))

    app.include_router(pages.router)
    app.include_router(chat_router.router)

    @app.middleware("http")
    async def revalidate_everything(request: Request, call_next):
        """
        Force browsers to revalidate, for the page as well as its assets.

        StaticFiles sends ETag and Last-Modified but no Cache-Control, and the
        rendered page sends neither, so browsers fall back to heuristic freshness
        and can serve either from cache long after it changed -- restarting the
        server does not help, because the browser never asks. The page and its
        scripts have to agree with each other, so staleness in one of them breaks
        the other; revalidating both is what keeps them in step.

        "no-cache" still permits caching; it only requires the ETag to be checked
        first, so unchanged files still come back as a cheap 304.

        A deployment that wants real caching should serve hashed filenames with a
        long max-age instead.
        """
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-cache"
        return response

    return app


server = create_app()
