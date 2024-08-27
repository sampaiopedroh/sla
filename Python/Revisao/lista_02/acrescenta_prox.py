def acrescenta(lista_nums):
    tam = len(lista_nums)
    ult = lista_nums[tam - 1]
    prox = ult + 1
    lista_nums.append(prox)
    return lista_nums

lista = [1,2,3]
teste = acrescenta(lista)
print(teste)
