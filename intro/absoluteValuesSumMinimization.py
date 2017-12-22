# Given a sorted array of integers a,
# find an integer x from a such that the value of
# 
# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
# 
# is the smallest possible (here abs denotes the absolute value).
# If there are several possible answers, output the smallest one.
# 
# Example
# 
# For a = [2, 4, 7], the output should be
# absoluteValuesSumMinimization(a) = 4.


def absoluteValuesSumMinimization(a):
    return a[len(a) // 2 + len(a) % 2 - 1]


#return a[b // 2 + b % 2 - 1]
#return A[(???(A)-1)//?]
#return A[???(A)//2-(???(A)%2==?)]
#----------
#?=len(A)
#    ?????? A[b // ? + b % 2 - ?]
#
#----------
#    rekord=10**10
#    ???=0
#    if a[len(?)-1]+1-a[0]<????:
#        for x in range(?[0],a[len(a)-?]+1):
#            summa=0
#            for ? in range(len(a)):
#                ?????+=abs(a[i]-x)
#           ?? summa<rekord:
#               rekord=summa
#                ???=x
#    else:
#         for x ?? range(-abs(sum(a)//???(a)+10),abs(sum(?)//len(a))+10):
#            summa=?
#            for i in range(???(a)):
#                summa+=abs(a[?]-x)
#            if summa<rekord:
#                ??????=summa
#                tal=x
#    return ???
#        
#    rekord=10**10
#    tal=0
#    if a[len(a)-1]+1-a[0]<1000:
#        for x in range(a[0],a[len(a)-1]+1):
#            summa=0
#            for i in range(len(a)):
#                rekord+=abs(a[i]-x)
#            if summa<rekord:
#                rekord=summa
#                tal=x
#    else:
#         for x in range(-abs(sum(a)//len(a)+10),abs(sum(a)//len(a))+10):
#            summa=0
#            for i in range(len(a)):
#                summa+=abs(a[i]-x)
#            if summa<rekord:
#                rekord=summa
#                tal=x
#    return tal
#    return a[(max(a)-1)//2 - (min(a)%2==0)]