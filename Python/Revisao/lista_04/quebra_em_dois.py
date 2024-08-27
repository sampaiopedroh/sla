def quebra(lista, num):
    menores = []
    maiores = []
    for i in range(len(lista)):
        if (lista[i] == num) or (lista[i] > num):
            maiores.append(lista[i])
        else:
            menores.append(lista[i])
    return f"maiores: {maiores} - menores: {menores}"

t_lista = [1,2,3,4,5,6,7,8,9]
teste = quebra(t_lista, 5)
print(teste)
