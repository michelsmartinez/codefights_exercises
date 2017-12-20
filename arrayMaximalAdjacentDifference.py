# Given an array of integers, find the maximal absolute
# difference between any two of its adjacent elements.
#
# Example
#
# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.


def arrayMaximalAdjacentDifference(inputArray):
    maximus = 0
    for i in range(1, len(inputArray)):
        dif = inputArray[i]-inputArray[i-1] if inputArray[i] >= inputArray[i-1] else inputArray[i-1]-inputArray[i]
        maximus = maximus if dif <= maximus else dif

    return maximus
