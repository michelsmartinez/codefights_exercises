#Given a rectangular matrix of characters, add a border of asterisks(*) to it.
#Example
#For
#picture = ["abc",
#           "ded"]
#
#the output should be
#addBorder(picture) = ["*****",
#                      "*abc*",
#                      "*ded*",
#                      "*****"]


def addBorder(picture):
    tamanho = len(picture[0]) + 2
    borded = ['*'*tamanho]
    for i in picture:
        borded.append("*" + i + "*")
    borded.append('*'*tamanho)

    return borded
