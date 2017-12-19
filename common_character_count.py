def commonCharacterCount(s1, s2):
    cont = 0
    for i in s1:
        if s2.count(i) > s1.count(i):
            cont += s1.count(i)
        else:
            cont += s2.count(i)
        s1 = s1.replace(i, '')
    return cont
