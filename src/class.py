from typing import List


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


if __name__ == '__main__':
    person: Person = Person("Jon Snow", 33)
    print(person.name)

    persons: List[Person] = [Person("Jon Snow", 33)]
    print(persons[0])

    persons.append(2)
    # IDE 提醒出错

