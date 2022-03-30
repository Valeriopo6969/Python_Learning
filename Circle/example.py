from circle import Circle

c1 = Circle(5, 3)
c2 = Circle(20, 1, True)
c3 = Circle(2, 1)
c4 = Circle(7, 2)

my_circles = Circle.sort_circles(c2, c1, c3, c4)

# Printing all circle from smaller to bigger
[Circle.print_circle(circle) for circle in my_circles]
