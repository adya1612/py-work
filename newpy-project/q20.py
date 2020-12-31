# checking in dict

print("This script will check if monument is present in dictionary")
print("It will add if not present and exit if monument is found.")

dictionary = {
        "Taj": "Agra",
        "Qutub-Minar": "Delhi",
        "Sun-Temple": "Puri"
    }
print(f"This is the dictionary: {dictionary}")

name = input("Enter the monument: ")

for i in dictionary:

    variable = ""

    if name != i and name != variable:
        variable = name
    else:
        print(dictionary)
        exit()

dictionary[name] = ""

print(dictionary)
