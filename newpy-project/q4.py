# to display the factorial of that number
import math

number = input("Enter the number: (should be a positive number)")
number = math.floor(float(number))


def factorial(n):

    n = number
    i = n - 1

    while n > i >= 2:
        n *= i
        i = i - 1
    return n


print(factorial(number))


# Cleaner version
# def fact(n):
#     if n <= 1:
#         return 1
#     return n*fact(n-1)
#
#
# if __name__ == '__main__':
#     print(f'Factorial: {fact(int(input("Enter number: ")))}')
