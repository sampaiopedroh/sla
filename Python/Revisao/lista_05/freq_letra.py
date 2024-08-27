def conta(string):
    count = {}
    for i in range(len(string)):
        char = string[i]
        if char in count:
            count[char] += 1
        else: 
            count[char] = 1

    mais = 0
    letra_mais_frequente = None
    
    for char in count:
        if count[char] > mais:
            mais = count[char]
            letra_mais_frequente = char
    
    return letra_mais_frequente

teste = conta("teste")
print(teste)

