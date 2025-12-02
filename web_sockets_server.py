import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получили сообщений: {message}")
        response = f"Сервер получил: {message}"
        await websocket.send(response)  # Отправляем ответ

# Запуск websocket сервера
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Websocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()

asyncio.run(main())
