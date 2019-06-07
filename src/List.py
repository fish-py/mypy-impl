from typing import List
"""
List的类型不兼容会导致运行时出错
"""


def greet_all(names: List[str]) -> None:
    for name in names:
        print('Hello ' + name)


if __name__ == '__main__':
    names: List[str] = ["Alice", "Bob", "Charlie"]
    ages: List[int] = [10, 20, 30]

    greet_all(names)  # Ok!
    greet_all(ages)  # Error due to incompatible types
