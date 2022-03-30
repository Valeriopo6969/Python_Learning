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
        circle_list = []
        [circle_list.append(_) for _ in args]
        circle_list.sort()
        return circle_list

    def is_point_inside_circle(self, x, y):
        radius = self.radius
        width = self.perimeter_width
        center = radius + width / 2
        distance = math.sqrt((x-center)**2 + (y-center)**2)
        # I'm drawing perimeter width on a range [-perimeter_width, perimeter_width] around the radius
        if (distance > radius - width / 2) & (distance < radius + width / 2):
            return True
        else:
            return False

    def print_circle(self):
        diameter = self.diameter
        width = self.perimeter_width
        for x in range(0, diameter + width):
            x_coord = x + 0.5
            for y in range(0, diameter + width):
                y_coord = y + 0.5
                if self.is_point_inside_circle(x_coord, y_coord):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print("")
