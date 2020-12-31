# function that counts the number of repetitions of the substrings in a given piece of string.

def count_number_of_the(user_letter):

    print(f"number of 'the' in string: {user_letter.count('the')}")
    print(f"number of 'The' in sting: {user_letter.count('The')}")


def invoke_function():
    count_number_of_the(input("Enter the string: "))


invoke_function()
