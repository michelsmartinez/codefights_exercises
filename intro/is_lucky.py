############Description#########################################################
#Ticket numbers usually consist of an even number of digits. A ticket number is#
#considered lucky if the sum of the first half of the digits is equal to the   #
#sum of the second half.                                                       #
#Given a ticket number n, determine if it's lucky or not.                      #
############Example#############################################################
#    For n = 1230, the output should be                                        #
#    isLucky(n) = true;                                                        #
#    For n = 239017, the output should be                                      #
#    isLucky(n) = false.                                                       #
################################################################################

def somalista(lista):
    soma = 0
    for x in lista:
        soma += int(x)
    return soma

def isLucky(n):
    sn = str(n)
    center = int(len(sn)/2)
    print("len:{}, {} | {}".format(center, sn[0:center], sn[center:]))
    total1 = somalista(sn[0:center])
    total2 = somalista(sn[center:])

    return total1 == total2
