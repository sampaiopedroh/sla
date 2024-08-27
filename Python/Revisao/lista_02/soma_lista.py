def soma_tudo(lista_nums):
    a = 0
    for i in range(len(lista_nums)):
                   a += lista_nums[i]
    return a

lista_teste = [1,2,3,4,5]
teste_def = soma_tudo(lista_teste)
print(teste_def)
