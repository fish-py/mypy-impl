from typing import Callable

"""
表明这个函数的参数是一个Callable（也就是函数了）
  这个Callable对象的参数是int, int,  返回值是str
"""
def do_add(add: Callable[[int, int], str], a: int, b: int) -> None:
    print(add(a, b))


def add(a: int, b: int) -> str:
    return str(a) + str(b)


if __name__ == '__main__':
    do_add(add, 1, 3)
