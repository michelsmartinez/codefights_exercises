# Given an array of equal-length strings, check if it is
# possible to rearrange the strings in such a way 
# that after the rearrangement the strings at consecutive
# positions would differ by exactly one character.
# 
# Example
# 
#     For inputArray = ["aba", "bbb", "bab"], the output should be
#     stringsRearrangement(inputArray) = false;
# 
#     All rearrangements don't satisfy the description condition.
# 
#     For inputArray = ["ab", "bb", "aa"], the output should be
#     stringsRearrangement(inputArray) = true.
# 
#     Strings can be rearranged in the following way: "aa", "ab", "bb".


from itertools import permutations

def isok(inputArray):
    for palavra in range(1, len(inputArray)):
        aux = 0
        for i in range(len(inputArray[palavra])):
            if inputArray[palavra][i] != inputArray[palavra - 1][i]:
                aux += 1
            if aux >= 2:
                return False
        if aux == 0:
            return False
    return True

def stringsRearrangement(inputArray):
    for testar in permutations(inputArray, len(inputArray)):
        if isok(testar):
            return True
    
    return False

