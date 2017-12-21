# An IP address is a numerical label assigned to each device
# (e.g., computer, printer) participating in a computer network that uses the
# Internet Protocol for communication.
# There are two versions of the Internet protocol,
# and thus two versions of addresses. One of them is the IPv4 address.
#
# IPv4 addresses are represented in dot-decimal notation,
# which consists of four decimal numbers, each ranging from 0 to 255 inclusive,
# separated by dots, e.g., 172.16.254.1.
#
# Given a string, find out if it satisfies the IPv4 address naming rules.


def isIPv4Address(inputString):
    lista = inputString.split('.')
    if len(lista) != 4:
        print ("len diferente")
        return False
    for i in lista:
        if not i.isnumeric():
            return False
        if int(i) not in range(0, 256):
            print ("outrange")
            return False
    return True
