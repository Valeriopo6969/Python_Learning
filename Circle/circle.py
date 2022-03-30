import math


class Circle:
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __init__(self, radius=None, perimeter_width=None, from_diameter=False):
        self.radius = radius if radius else 1
        self.radius = math.floor(radius * 0.5) if from_diameter else radius
        self.perimeter_width = perimeter_width if perimeter_width else 1

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @classmethod
    def sort_circles(cls, *args):
        circle_list = [circle for circle in args]
        circle_list.sort()
        return circle_list

    def is_point_inside_circle(self, x, y):
        radius = self.radius
        width = self.perimeter_width
        center = radius + width / 2
        distance = math.sqrt((x-center)**2 + (y-center)**2)

        # I'm drawing perimeter width on a range [-perimeter_width, perimeter_width] around the radius
        return (distance > radius - width / 2) & (distance < radius + width / 2)

    def print_char(self, x_coord, y_coord):
        char = "*" if self.is_point_inside_circle(x_coord, y_coord) else " "
        print(char, end=" ")

    def print_circle(self):
        diameter = self.diameter
        width = self.perimeter_width
        char_to_draw = diameter + width

        for x in range(char_to_draw):
            [self.print_char(x+0.5, y+0.5) for y in range(char_to_draw)]
            print()
