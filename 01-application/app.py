from flask import Flask, request
import os
import socket

app = Flask(__name__)

@app.route('/')
def info():
    # Получаем имя хоста
    hostname = socket.gethostname()
    # Получаем IP-адрес хоста
    ip_address = socket.gethostbyname(hostname)
    # Получаем имя автора из переменной окружения
    author = os.getenv('AUTHOR', 'Не указано')

    # Формируем HTML-страницу
    response = f"""
    <html>
        <head><title>Информация о хосте</title></head>
        <body>
            <h1>Информация о хосте</h1>
            <p><strong>Имя хоста:</strong> {hostname}</p>
            <p><strong>IP-адрес:</strong> {ip_address}</p>
            <p><strong>Имя автора:</strong> {author}</p>
        </body>
    </html>
    """
    return response

@app.route('/healthz')
def healthz():
    # Простой эндпоинт для liveness-пробы
    return "OK", 200

@app.route('/readyz')
def readyz():
    # Простой эндпоинт для readiness-пробы
    # По хорошему тут что то проверить (например подключение к бд)
    return "Ready", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)