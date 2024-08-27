def soma(lista_nums):
    a = 0
    for i in range(len(lista_nums)):
        a+=lista_nums[i]
    return a

def media(lista_nums):
    result_soma = soma(lista_nums)
    divisor = len(lista_nums)
    resultado = result_soma / divisor
    return resultado

lista = [1,2,3,4,5]
teste = media(lista)
print(teste)
