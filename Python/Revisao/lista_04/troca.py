def troca(lista, pos1, pos2):
    aux = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = aux
    return lista

t_lista = [1,2,3]
teste = troca(t_lista, 0, 2)
print(teste)

