# sum of numbers

def number_operation(user_number):
    numbers = list(map(int, user_number.split()))

    sum_of_positive_even_numbers = 0
    sum_of_positive_odd_numbers = 0
    sum_of_negative_numbers = 0

    for i in numbers:
        if i > 0 and i % 2 == 0 and i != 0:
            sum_of_positive_even_numbers += i
            print(f"The sum of positive even numbers is: {sum_of_positive_even_numbers}")
            print(f"The sum of positive odd numbers is: {sum_of_positive_odd_numbers}")
            print(f"The sum of negative numbers is: {sum_of_negative_numbers}")
        elif i > 0 and i % 2 != 0 and i != 0:
            sum_of_positive_odd_numbers += i
            print(f"The sum of positive even numbers is: {sum_of_positive_even_numbers}")
            print(f"The sum of positive odd numbers is: {sum_of_positive_odd_numbers}")
            print(f"The sum of negative numbers is: {sum_of_negative_numbers}")
        elif i != 0:
            sum_of_negative_numbers += i
            print(f"The sum of positive even numbers is: {sum_of_positive_even_numbers}")
            print(f"The sum of positive odd numbers is: {sum_of_positive_odd_numbers}")
            print(f"The sum of negative numbers is: {sum_of_negative_numbers}")
        else:
            exit()


print("Enter the numbers. Hit SPACE. Don't hit ENTER")
print("Another thing. Whenever you input zero & hit ENTER, the script won't consider the succeeding numbers.")
print("So, be careful :) ")
number_operation(input("Enter the numbers ---> "))
