from math import pi


class Circle:
    r: float

    def __init__(self, r: float) -> None:
        self.r = r

    def area(self) -> float:
        area: float = 0.0
        area = pi * (self.r**2)
        return area


class Rectangle:
    h: float
    w: float

    def __init__(self, h: float, w: float) -> None:
        self.h = h
        self.w = w

    def area(self) -> float:
        area: float = 0.0
        area = self.h * self.w
        return area


circ: Circle = Circle(r=2.0)
print(circ.area())
rect: Rectangle = Rectangle(w=4.0, h=5.5)
print(rect.area())
