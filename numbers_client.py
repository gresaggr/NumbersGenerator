import requests

BASE_URL = "http://127.0.0.1:8000"


def just_number(number):
    return requests.post(f"{BASE_URL}/just_number/", params={"number": number})


def array_numbers(numbers):
    return requests.post(f"{BASE_URL}/array_numbers/", json=numbers)  # json вместо params потому что список


def custom_range(start, end):
    return requests.post(f"{BASE_URL}/custom_range/", params={"start": start, "end": end})


if __name__ == "__main__":
    try:
        my_number = 15
        response = just_number(my_number)
        print(f'Для запроса одного числа {my_number} ответ: {response.json()}')
    except Exception as e:
        print(f'Ошибка запроса для одного числа: {e}')

    my_array = [1, 3, 5, 6, 9, 10, 12, 13, 15]
    try:
        response = array_numbers(my_array)
        print(f'Для запроса массива {my_array} ответ: {response.json()}')
    except Exception as e:
        print(f'Ошибка запроса для массива: {e}')

    my_range = (1, 10)
    try:
        response = custom_range(*my_range)
        print(f'Для запроса промежутка {my_range} ответ: {response.json()}')
    except Exception as e:
        print(f'Ошибка запроса для промежутка: {e}')
