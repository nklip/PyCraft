"""WebSocket transport. Receives, validates, dispatches, sends the reply back."""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import ValidationError

from app.chat import intents
from app.chat.connections import ConnectionManager, WebSocketConnectionModel
from app.chat.schemas import Payload

router = APIRouter()

manager = ConnectionManager()


@router.websocket("/communicate")
async def communicate(websocket: WebSocket, client_id: str):
    print("Endpoint '/communicate' called...")
    await manager.connect(websocket, client_id)

    try:
        while True:
            data = await websocket.receive_json()

            try:
                payload = Payload.model_validate(data)
            except ValidationError as error:
                # A malformed message is the client's problem, not a reason to
                # drop the connection -- tell the user and keep listening.
                print(f"Rejected malformed payload from '{client_id}': {error}")
                await manager.send_personal_message(
                    intents.text_reply("Sorry, I could not read that message."),
                    client_id,
                )
                continue

            reply = intents.handle(payload, client_id)
            bot_response = manager.create_json_response(reply, "bot")
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
