a: int = 3

b: str

c: float

d: bool

if __name__ == '__main__':
    a: int = 3
    print(a)

    # 运行时不会报错，但是IDE会有智能提醒
    a = "sdf"
    print(a)

