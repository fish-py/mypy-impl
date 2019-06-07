def add(a: int, b: int) -> int:
    return a + b


def run() -> None:
    print("I am running")


if __name__ == '__main__':
    sum_ = add(1, 2)
    print(sum)

    add(1, 3)

    sum_ = add("a", "b")
    print(sum)

    res = run()
