def maior(a,b,c,d):
    maior = d
    if (a > b) and (a > c) and (a > d):
        maior = a
    elif (b > c) and (b > d):
        maior = b
    elif c > d:
        maior = c
    return maior

teste1 = maior(1,2,3,4)
teste2 = maior(4,3,2,1)
teste3 = maior(1,4,2,3)
teste4 = maior(2,1,4,3)
print(teste1, teste2, teste3, teste4)
