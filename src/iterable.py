from typing import Iterable, TypeVar


"""
定义一个泛型对象
"""
T = TypeVar('T')

"""
Iterable 对象
"""
def print_all(s: Iterable[T]):
    for item in s:
        print(item)


if __name__ == '__main__':
    list1 = ["a", "b"]
    print_all(list1)

    list2 = [1, "2"]
    print_all(list2)

