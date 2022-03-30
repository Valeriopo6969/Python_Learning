# About 
This exercise consist on having a [class](https://github.com/Valeriopo6969/Python_Learning/blob/main/Circle/circle.py) representing a simple circle.

## Features
 * A <b>Circle</b> can be defined by either specifying the radius or the diameter:
```python
    my_circle_from_radius = Circle(5) # my_circle.radius = 5
 
    my_circle_from_diameter = Circle(5, 1, True) # my_circle.radius = 2.5
```
 * Get the circle's <b>Area</b>. (π*r^2)
```python
    my_circle_area = my_circle.area
```
 * Print the circle and get something nice... or at least i've tried :P 
  ```python
      # Second parameter is for setting visual perimeter width, more on the actual script
      circle_1 = Circle(7, 2)
      circle_2 = Circle(20, 1, True)
      
      my_circles = [circle_1, circle_2]
      [Circle.print_circle(circle) for circle in my_circles]
```
<img src="https://github.com/Valeriopo6969/Python_Learning/blob/main/Circle/print_example.jpg">

 * Able to add two circles together
 * Able to compare two circles to see which is bigger
 * Able to see if they are equal

## <b>Testing functionality [here](https://github.com/Valeriopo6969/Python_Learning/blob/main/Circle/circle_test.py)</b>
## <b>Example of usage [here](https://github.com/Valeriopo6969/Python_Learning/blob/main/Circle/example.py)</b>
