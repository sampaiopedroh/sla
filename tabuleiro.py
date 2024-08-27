def tabuleiro_xadrez(tamanho):
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            if (i + j) % 2 == 0:
                linha.append(".")
            else:
                linha.append("x")
        tabuleiro.append(linha)
    return tabuleiro

teste = tabuleiro_xadrez(4)
print(teste)
