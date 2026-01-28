import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Hello, server!"
        print(f"Отправили: {message}")
        await websocket.send(message)  # отправили сообщение

        response = await websocket.recv()  # получаем ответ от сервера
        print(f"Ответ получен: {response}")

asyncio.run(client())
