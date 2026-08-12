"""WebSocket transport. Receives, validates, dispatches, sends the reply back."""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import ValidationError

from app.chat import messages, modes
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
                    manager.create_json_response(
                        {"message": messages.text("Sorry, I could not read that message.")},
                        "bot",
                    ),
                    client_id,
                )
                continue

            print(f"Message from '{client_id}': {payload.text!r}")
            reply = manager.create_json_response({"message": modes.dispatch(payload.text)}, "bot")
            await manager.send_personal_message(reply, client_id)
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
