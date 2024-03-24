from fastapi import FastAPI
import uvicorn

from numbers_generator import get_answer

app = FastAPI()


@app.post("/just_number/")
async def just_number(number: int):
    return get_answer(number)


@app.post("/array_numbers/")
async def array_numbers(numbers: list[int]):
    return [get_answer(number) for number in numbers]


@app.post("/custom_range/")
async def custom_range(start: int, end: int):
    return [get_answer(number) for number in range(start, end + 1)]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
