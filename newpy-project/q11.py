# to count the number of positive and negative numbers

def count_positive_and_negative(user_number):

    number = list(map(int, user_number.split()))

    positive_count = 0
    negative_count = 0

    for i in number:
        if i > 0:
            positive_count += 1
        else:
            negative_count += 1

    print(f"Total positive numbers: {positive_count}")
    print(f"Total negative numbers: {negative_count}")


def invoke_function():
    print("Enter the numbers. Hit SPACE. Don't hit ENTER.")
    count_positive_and_negative(input("Enter the list of numbers: "))


invoke_function()
