def new_format(num: str) -> str:
    num = num[::-1]
    return '.'.join([num[i:i + 3] for i in range(0, len(num), 3)])[::-1]


if __name__ == "__main__":
    assert (new_format("123456789") == "123.456.789")
    assert (new_format("100") == "100")
    assert (new_format("1000") == "1.000")
    assert (new_format("100000") == "100.000")
    assert (new_format("10000") == "10.000")
    assert (new_format("0") == "0")
    print('Correct!')
