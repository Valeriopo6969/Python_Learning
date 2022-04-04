from circle import Circle

c1 = Circle(5, 3)
c2 = Circle.from_diameter(20, 1)
c3 = Circle(2, 1)
c4 = Circle(7, 2)

my_circles = [c1, c2, c3, c4]
my_circles.sort()

# Printing all circle from smaller to bigger
[Circle.print_circle(circle) for circle in my_circles]
