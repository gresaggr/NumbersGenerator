import asyncio
import websockets
import json

from numbers_generator import get_answer


async def process_command(command):
    if command["type"] == "just_number":
        number = command["number"]
        # if not isinstance(number, int):
        #     return 'Должно быть целое число!'
        return get_answer(number)

    if command["type"] == "array_numbers":
        numbers = command["numbers"]
        return [get_answer(number) for number in numbers]

    if command["type"] == "custom_range":
        start = command["start"]
        end = command["end"]
        return [get_answer(number) for number in range(start, end + 1)]

    return "Не известная команда!"


async def websocket_handler(websocket, path):
    async for message in websocket:
        command = json.loads(message)
        print(f'Пришла команда: {command}')
        response = await process_command(command)
        print(f'Ответ: {response}')
        await websocket.send(json.dumps(response))


print('Запущен WS сервис')
start_server = websockets.serve(websocket_handler, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
