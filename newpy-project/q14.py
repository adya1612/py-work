# checking using for loop

def checking_number_presence(number_list, number):

    list_of_number = list(map(float, number_list.split()))

    for i in list_of_number:
        if i == float(number):
            print("This is the number in the list you were looking for: ")
            print(i)


checking_number_presence(input("Enter the list of numbers: "), input("Enter the search number: "))
