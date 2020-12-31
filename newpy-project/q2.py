# we can calculate the area of a triangle with its given 3 sides using heron's formula
import math

a = input("This is the first side of the triangle. Enter the number:")
b = input("This is the second side of the triangle. Enter the number:")
c = input("This is the third side of the triangle. Enter the number:")

perimeter = float(a) + float(b) + float(c)
print(f"the perimeter of the triangle is: {perimeter}")

perimeter = perimeter/2

a = perimeter - float(a)
b = perimeter - float(b)
c = perimeter - float(c)

area = math.sqrt(perimeter*a*b*c)

print(f"The area of the triangle is: {area}")
