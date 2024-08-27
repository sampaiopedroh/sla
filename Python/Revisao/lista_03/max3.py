def maior(a,b,c):
    maior = c
    if (a > b) and (a > c):
        maior = a
    elif b > c:
        maior = b
    return maior

teste1 = maior(1,2,3)
teste2 = maior(3,2,1)
teste3 = maior(2,1,3)
print(teste1, teste2, teste3)
