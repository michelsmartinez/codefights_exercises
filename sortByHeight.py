"""
Some people are standing in a row in a park.
There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights
in a non-descending order without moving the trees.

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""


def sortByHeight(a):
    lista = sorted(a)
    j = 0
    for i in lista:
        if i != -1:
            while a[j] == -1:
                j += 1
            a[j] = i
            j += 1

    return a
