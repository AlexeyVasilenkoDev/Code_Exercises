link = "https://www.codewars.com/kata/5ace2d9f307eb29430000092"


def modify_multiply(st: str, loc: int, num: int):
    result = [st.split(' ')[loc] for _ in range(num)]
    return '-'.join(result)
