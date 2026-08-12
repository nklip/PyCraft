"""WebSocket transport. Receives, validates, dispatches, sends the reply back."""

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import ValidationError

from app.chat import messages, modes
from app.chat.connections import ConnectionManager
from app.chat.schemas import Payload

router = APIRouter()

manager = ConnectionManager()


@router.websocket("/communicate")
async def communicate(websocket: WebSocket, client_id: str):
    connection = await manager.connect(websocket, client_id)
    conversation = connection.conversation
    session_id = connection.session_id

    async def say(message: dict) -> None:
        await manager.send_personal_message(
            manager.create_json_response({"message": message}, "bot"), session_id
        )

    try:
        while True:
            data = await websocket.receive_json()

            try:
                payload = Payload.model_validate(data)
            except ValidationError as error:
                # A malformed message is the client's problem, not a reason to
                # drop the connection -- tell the user and keep listening.
                print(f"Rejected malformed payload on session {session_id}: {error}")
                await say(messages.text("Sorry, I could not read that message."))
                continue

            print(f"Session {session_id}: {payload.text!r}")
            await say(await modes.dispatch(payload.text, conversation))
    except WebSocketDisconnect as web_ex:
        if web_ex.code in (1000, 1001):
            print("Session finished.")
        else:
            print(f"Error in session {session_id}: {web_ex}")
    except Exception as ex:
        # Say something before going quiet. Swallowing this leaves the browser
        # waiting on a reply that will never arrive, which reads as a frozen
        # chat rather than an error -- and hides the bug that caused it.
        print(f"An error has occured on session {session_id}: {ex!r}")
        try:
            await say(messages.text("Something went wrong on my side. Please try again."))
        except Exception:
            pass  # The socket is already gone; nothing left to tell.
    finally:
        # Always, so a conversation cannot outlive the tab that owns it.
        manager.disconnect(session_id)
