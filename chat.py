from collections import defaultdict

from fastapi import FastAPI, Path
from starlette.websockets import WebSocket

app = FastAPI()


chats = defaultdict(list)


@app.websocket('/ws/{chat_id}')
async def chat(websocket: WebSocket, chat_id: int = Path()):
    await websocket.accept()
    chats[f'{chat_id}'].append(websocket)
    while True:
        data = await websocket.receive_text()
        for user in chats[f'{chat_id}']:
            await user.send_text(data)
