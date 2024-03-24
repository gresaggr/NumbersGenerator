START_CHECK_RANGE = 1
END_CHECK_RANGE = 1000


def get_answer(num: int) -> str | int:
    if num % 3 == 0 and num % 5 == 0:
        res = 'МаркоПолло'
    elif num % 3 == 0:
        res = 'Марко'
    elif num % 5 == 0:
        res = 'Полло'
    else:
        res = num

    return res


def main():
    for num in range(START_CHECK_RANGE, END_CHECK_RANGE + 1):
        print(get_answer(num))


if __name__ == "__main__":
    main()
