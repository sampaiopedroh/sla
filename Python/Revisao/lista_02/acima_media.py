def acima_media(lista, media):
    lista_acima = []
    for i in range(len(lista)):
        if lista[i] > media:
            lista_acima.append(lista[i])
    return lista_acima

media = 4
lista = [1,2,3,4,5,6,7,8,9]
teste = acima_media(lista, media)
print(teste)
