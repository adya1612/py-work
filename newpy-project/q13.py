# average of elements:

def average():
    list_numbers = [25, 45, 12, 45, 85, 25]
    print("This is the given list of numbers: ")
    print(list_numbers)

    total = 0

    for i in list_numbers:
        total += i
    total /= len(list_numbers)
    print(f"The average of the numbers are: {total}")


average()
