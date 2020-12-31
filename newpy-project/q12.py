# function accepts a list of strings as arguments and displays the strings which starts with a or A.

def show_a(user_word):

    word = list(map(str, user_word.split()))
    print(word)

    for i in word:
        if i[0] == 'A' or i[0] == 'a':
            print(i)


def invoke_function():
    print("This program accepts a list of strings as arguments and displays the strings which starts with a or A.")
    show_a(input("Enter words: "))


invoke_function()
