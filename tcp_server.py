import socket


def server():
    # Создаем TCP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем его к адресу проекта
    server_address = ("localhost", 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения
    server_socket.listen(5)
    print("Сервер запущен и ждет подключения ...")

    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        # Получение данных от клиента
        data = client_socket.recv(1024).decode()
        print(f"Получены данные: {data}")

        # Отправляем ответ клиенту
        response = f"Отправляем: {data}"
        client_socket.send(response.encode())

        # Закрываем соединение с клиентом
        client_socket.close()

if __name__ == "__main__":
    server()
