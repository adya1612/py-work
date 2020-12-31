# dictionary operation

common_knowledge = {}


def country_capital():

    for i in range(1, 6):
        temp_storage = input("Enter country name, capital name: ").split(',')
        common_knowledge[temp_storage[0]] = temp_storage[1]
    print(common_knowledge)


country_capital()
