import math
from circle import Circle


def test_correct_circle_from_radius():
    my_circle = Circle(5)
    assert my_circle.radius == 5
    assert my_circle.diameter == 10


def test_correct_circle_from_diameter():
    my_circle = Circle.from_diameter(10)
    assert my_circle.radius == 5
    assert my_circle.diameter == 10


def test_correct_circle_area():
    my_circle = Circle(5)
    assert my_circle.area == math.pi * my_circle.radius ** 2


def test_correct_sum_between_circles():
    my_circle_0 = Circle(5)
    my_circle_1 = Circle(3)
    assert (my_circle_1 + my_circle_0).radius == 8


def test_correct_bigger_circle():
    my_bigger_circle = Circle(5)
    my_smaller_circle = Circle(3)
    assert my_bigger_circle > my_smaller_circle


def test_correct_equal_circles():
    my_circle_0 = Circle(5)
    my_circle_1 = Circle(5)
    assert my_circle_1 == my_circle_0


def test_correct_circle_sorting():
    my_circle_0 = Circle(1)
    my_circle_1 = Circle(2)
    my_circle_2 = Circle(3)
    my_circles = [my_circle_0, my_circle_1, my_circle_2]
    my_circles.sort()
    assert my_circles[0] == my_circle_0
    assert my_circles[1] == my_circle_1
    assert my_circles[2] == my_circle_2
