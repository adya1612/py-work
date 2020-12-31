# function that takes string as arg & returns the number of vowels and consonants when invoked.


def vowel_count(wo):
    vowels = ('a', 'e', 'i', 'o', 'u')
    b = list(wo)
    print(b)

    for i in list(wo):
       if i in vowels:
           b.remove(i)
    # print(len(b))
    # length of total consonants
    # print(len(wo) - len(b))
    # length of vowels
    return (len(wo) - len(b)), len(b)


res = (vowel_count(input("enter word: ")))
print(f"consonants: {res[1]}")
print(f"vowels: {res[0]}")


