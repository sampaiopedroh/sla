def menor(lista):
    i_menor = 0
    for i in range(len(lista)):
        if lista[i_menor] > lista[i]:
            i_menor = i
    return i_menor

t_lista = [1,2,3,4,0]
teste = menor(t_lista)
print(teste)
