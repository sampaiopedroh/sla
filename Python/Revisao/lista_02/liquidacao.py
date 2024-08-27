def liquidacao(preco, des):
    precos_novos = []
    for i in range(len(preco)):
        precos_novos.append(preco[i]-des[i])
    return precos_novos

precos = [9,8,7,6,5,4,3,2,1]
descontos = [1,2,3,1,2,3,1,2,3]
teste = liquidacao(precos, descontos)
print(teste)
