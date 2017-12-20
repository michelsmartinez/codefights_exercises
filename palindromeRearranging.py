# Given a string, find out if its characters can be rearranged to form a palindrome.
# Example
# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.
# We can rearrange "aabb" to make "abba", which is a palindrome.


def palindromeRearranging(inputString):
    print (inputString)
    center = 0
    for i in inputString:
        if inputString.count(i)%2!=0:
            center += 1
            if center > 1:
                return False
    inputString = inputString.replace(i, '')
    return True

