# function that takes string as an arg and replaces all capital alphabets with small alphabets.

def lower_case(user_word):

    b = ""
    c = list(b)

    for i in list(user_word):
        if i.isupper():
            c.extend(i.lower())
        else:
            c.extend(i)
    print(b.join(c))


# lower_case(input("Enter word: "))


def invoke_function():
    lower_case(input("Enter the word: "))


invoke_function()
