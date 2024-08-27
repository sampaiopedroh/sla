def anag(p1, p2):
    if len(p1) != len(p2):
        return False
    
    count_p1 = {}
    count_p2 = {}
    
    for i in range(len(p1)):
        char = p1[i]
        if char in count_p1:
            count_p1[char] += 1
        else:
            count_p1[char] = 1
    
    for i in range(len(p2)):
        char = p2[i]
        if char in count_p2:
            count_p2[char] += 1
        else:
            count_p2[char] = 1

    if count_p1 == count_p2:
        return True
    return False

teste = anag("tests", "teste")
print(teste)

