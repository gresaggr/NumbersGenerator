import asyncio
import websockets
import json

URI = "ws://localhost:8765"


async def send_command(uri, command):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(command))
        return await websocket.recv()


async def main():
    print('Запущен клиент WS для проверки генерации номеров.')

    my_number = 15
    try:
        response = await send_command(URI, {"type": "just_number", "number": 9})
        print(f'Для запроса одного числа {my_number} ответ: {json.loads(response)}')
    except Exception as e:
        print(f'Ошибка запроса для одного числа: {e}')

    my_array = [1, 3, 5, 6, 9, 10, 12, 13, 15]
    try:
        response = await send_command(URI, {"type": "array_numbers", "numbers": my_array})
        print(f'Для запроса массива {my_array} ответ: {json.loads(response)}')
    except Exception as e:
        print(f'Ошибка запроса для массива: {e}')

    my_range = (1, 10)
    try:
        response = await send_command(URI, {"type": "custom_range", "start": 1, "end": 10})
        print(f'Для запроса промежутка {my_range} ответ: {json.loads(response)}')
    except Exception as e:
        print(f'Ошибка запроса для промежутка: {e}')


if __name__ == "__main__":
    asyncio.run(main())
