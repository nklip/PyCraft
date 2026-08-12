
import os
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from connection_manager import ConnectionManager, WebSocketConnectionModel

BASE_DIR = Path(__file__).resolve().parent

server = FastAPI()
server.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
server.mount("/chatbot/static", StaticFiles(directory=str(Path(BASE_DIR, 'static'))), name="static")

templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

manager = ConnectionManager()

profile = os.environ["PROFILE"]
ws_host = os.environ["WS_HOST"]

from models import Payload

def process_message(payload: Payload, client_id):
    response = {
        "type": "bot",
        "message": "Not implemented"
    }

    print(f"Processing message: '{payload}' for user = '{client_id}'")

    intent = payload["intent"]

    if intent == "table":
        payload["message"] = {
            "template_type": "table",
            "clickable": "false",
            "text": "This table contains next values.",
            "msg_payload" : [
                {
                    "Type": "Corporation",
                    "RowIndex": 1,
                    "Id": "1",
                    "Name": "Umbrealla corporation"
                },
                {
                    "Type": "Corporation",
                    "RowIndex": 2,
                    "Id": "2",
                    "Name": "Apple INC"
                },
                {
                    "Type": "Bank",
                    "RowIndex": 3,
                    "Id": "3",
                    "Name": "Citi"
                },
                {
                    "Type": "Bank",
                    "RowIndex": 4,
                    "Id": "4",
                    "Name": "JPMC"
                },
                {
                    "Type": "Bank",
                    "RowIndex": 5,
                    "Id": "5",
                    "Name": "Barclays"
                },
                {
                    "Type": "Bank",
                    "RowIndex": 6,
                    "Id": "6",
                    "Name": "Bank of Scotland"
                }
            ]
        }
    else:
        payload["message"] = {
            "template_type" : "text",
            "text" : "This message is from backend, ohoho!"
        }
    response = payload;
    return response

@server.get("/chatbot")
async def home(request: Request):
    print("Starting chatbot...")
    return templates.TemplateResponse(
        request = request, name = "index.html", context = {
            "src" : "chatbot/static",
            "profile" : profile,
            "ws_host" : ws_host,
            "soeid" : "nl0000"
        }
    )

@server.websocket("/communicate")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    print("Endpoint '/communicate' called...")
    await manager.connect(websocket, client_id)

    try:
        while True:
            data = await websocket.receive_json()
            response = process_message(data, client_id)
            bot_response = manager.create_json_response(response, "bot")
            print(f"Bot response message: '{bot_response}' for user = '{client_id}'")
            await manager.send_personal_message(bot_response, client_id)
    except WebSocketDisconnect as web_ex:
        connection = WebSocketConnectionModel()
        connection.client_id = client_id
        connection.socket = websocket
        manager.disconnect(connection)

        if web_ex.code in (1000, 1001):
            print("Session finished.")
        else:
            print(f"Error in Session: {web_ex}")
    except Exception as ex:
        print(f"An error has occured while trying to establish WS connection: {ex}")



async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world! Great me!',
    })
