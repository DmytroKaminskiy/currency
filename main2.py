class Shape:
    def area(self):
        raise NotImplementedError()

    def perimeter(self):
        raise NotImplementedError()


class Circle(Shape):
    pass


class Rectangular(Shape):
    pass


class Triangle(Shape):
    pass


if __name__ == '__main__':
    r = Rectangular(2, 4)
    assert r.area() == 8
    assert r.perimeter() == 12
