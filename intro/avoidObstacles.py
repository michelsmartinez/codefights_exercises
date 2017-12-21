# You are given an array of integers representing coordinates of obstacles
# situated on a straight line.
#
# Assume that you are jumping from the point with coordinate 0 to the right.
# You are allowed only to make jumps of the same
# length represented by some integer.
#
# Find the minimal length of the jump enough to avoid all the obstacles.
#
# Example
#
# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.


def passatudo(pode, quantos):
    aux = 0
    while pode[aux] != True:
        aux += 1
    while aux < len(pode):
        if pode[aux] == False:
            return False
        aux += quantos
    return True


def avoidObstacles(inputArray):
    tamanho = sorted(inputArray)[-1] + 2
    pode = {}
    for i in range(0, tamanho):
        pode[i] = False if i in inputArray else True
    print (pode)
    for i in range(1, tamanho):
        if passatudo(pode, i):
            return i
    return 0

