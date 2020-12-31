# counting duplicates

import collections


def count_duplicates(elements):
    element_list = list(map(int, elements.split()))
    a = collections.defaultdict(int)

    for elements in element_list:
        a[elements] += 1
        if a[elements] > 1:
            print(f"The element {elements} is repeated a total of {a[elements]} times.")


count_duplicates(input("Enter the list of elements: "))
