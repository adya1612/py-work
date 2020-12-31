# general formula for quadratic equation:
# a(x^2) + bx + c = 0
import math

print("The general formula for a quadratic equation is: a(x^2) + bx + c = 0")
print("You will have to enter the numbers a, b and c")

a = input("Enter the value of a:")
b = input("Enter the value of b:")
c = input("Enter the value of c:")


root_1 = (-float(b)) + (math.sqrt(4*float(a)*float(c)))
root_1 = root_1/(2*float(a))

root_2 = (-float(b)) - (math.sqrt(4*float(a)*float(c)))
root_2 = root_2/(2*float(a))

print(f"Here are the solutions: {root_2} & {root_1}")
