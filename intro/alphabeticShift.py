# Given a string, replace each its character 
# by the next one in the English alphabet (z would be replaced by a).
# 
# Example
# 
# For inputString = "crazy", the output should be
# alphabeticShift(inputString) = "dsbaz".


def alphabeticShift(inputString):
    alfabet = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k','k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p':'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'a'}
    outputString = ""
    for i in range(len(inputString)):
        outputString += alfabet[inputString[i]]
    
    return outputString