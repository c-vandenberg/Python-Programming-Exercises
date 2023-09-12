#!/usr/bin/env python3

from shape_class_subclass import Square, Rectangle, Circle


def main():
    square: Square = Square(5.00)
    print(square.calculate_area())

    rectangle: Rectangle = Rectangle(10.00, 5.00)
    print(rectangle.calculate_area())

    circle: Circle = Circle(2.50)
    print(format(circle.calculate_area(), ".2f"))


if __name__ == '__main__':
    main()
