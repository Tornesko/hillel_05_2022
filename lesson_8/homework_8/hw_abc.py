from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("----", "|  |", "----", sep="\n")


class Circle(Shape):
    def draw(self):
        print(" -- ", "-  -", " -- ", sep="\n")


def get_shape(cls) -> Shape:
    options: list[Shape] = [Rectangle(), Circle()]
    return choice(options).draw()


def main():
    get_shape(Shape)


if __name__ == "__main__":
    main()
