def conta(string):
    dicti = {}
    for i in range(len(string)):
        char = string[i]
        if char in dicti:
            count[char] += 1
        else:
            count[char] = 1
    return dicti

teste = conta("sla")
print(teste)
