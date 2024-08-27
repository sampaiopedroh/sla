def maior(a,b,c,d,e):
    maior = e
    if (a>b) and (a>c) and (a>d) and (a>e):
        maior = a
    elif (b>c) and (b>d) and (b>e):
        maior = b
    elif (c>d) and (c>e):
        maior = c
    elif d > e:
        maior = d
    return maior

teste = maior(1,2,3,5,4)
print(teste)
