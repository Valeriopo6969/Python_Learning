import math


class Circle:
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __init__(self, radius, perimeter_width=1):
        self.radius = radius
        self.perimeter_width = perimeter_width

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    @classmethod
    def from_diameter(cls, diameter, perimeter_width=1):
        return Circle(diameter * 0.5, perimeter_width)

    def is_point_inside_circle(self, x, y):
        radius = self.radius
        half_width = self.perimeter_width * 0.5
        center = radius + half_width
        distance = math.sqrt((x-center)**2 + (y-center)**2)

        # I'm drawing perimeter width on a range [-perimeter_width, perimeter_width] around the radius
        return (distance > radius - half_width) & (distance < radius + half_width)

    def print_char(self, x_coord, y_coord):
        char = "*" if self.is_point_inside_circle(x_coord, y_coord) else " "
        print(char, end=" ")

    def print_circle(self):
        diameter = self.diameter
        width = self.perimeter_width
        char_to_draw = math.ceil(diameter + width)  # can be perfect by checking when to ceil and when to floor

        for x in range(char_to_draw):
            for y in range(char_to_draw):
                self.print_char(x + 0.5, y + 0.5)
            print()
