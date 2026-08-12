"""HTML routes."""

from fastapi import APIRouter, Request

from app.settings import STATIC_URL, settings

router = APIRouter()

# Assigned by create_app(), which owns the template directory.
templates = None


@router.get("/chatbot")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "static_url": STATIC_URL,
            "profile": settings.profile,
            "ws_host": settings.ws_host,
            "soeid": "nl0000",
        },
    )
