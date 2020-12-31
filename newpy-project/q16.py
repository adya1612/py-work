# average of elements:


def average():
    tuple_numbers = (25, 45, 12, 45, 85, 25)
    print(f"This is the given tuple of numbers:\n {tuple_numbers}")

    total = 0

    for i in tuple_numbers:
        total += i
    total /= len(tuple_numbers)
    print(f"The average of the given tuple of numbers is: {total}")


average()
