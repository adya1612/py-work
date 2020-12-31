# to find the maximum and the minimum of the numbers in a list

def max_min(number):

    numbers = list(map(int, number.split()))

    numbers.sort()

    print(f"The smallest number is: {numbers[0]}")
    print(f"The largest number is: {numbers[-1]}")


def invoke_function():
    print("after entering each number hit space (NOT ENTER)")
    max_min(input("Enter the numbers: "))


invoke_function()
