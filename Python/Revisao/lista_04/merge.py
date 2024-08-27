def merge(lista1, lista2):
    i1 = 0
    i2 = 0
    lista_conjunta = []
    tam = len(lista2)
    if len(lista1) > len(lista2):
        tam = len(lista1)
    for i in range(tam):
        if lista1[i1] == lista2[i2]:
            lista_conjunta.append(lista1[i1])
        elif lista1[i1] > lista2[i2]:
            lista_conjunta.append(lista2[i2])
            i2+=1
        else:
            lista_conjunta.append(lista1[i1])
            i1+=1
    return lista_conjunta

t_l1 = [1,2,3,4,5,6,7,8,9]
t_l2 = [9,8,7,6,5,4,3,2,1]
teste = merge(t_l1, t_l2)
print(teste)
