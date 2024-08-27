# matriz = [
#[1,2,3]
#[4,5,6]
#[7,8,9]
#]

# matriz = [[1,2,3], [4,5,6], [7,8,9]]

# linha e colunas aleatórias
def criar_matriz(linhas, colunas):
    matriz = [["." for _ in range(colunas)] for _ in range(linhas)]
#    return "\n".join([" ".join(linha) for linha in matriz])
    return matriz
resultado = criar_matriz(3, 4)
print(resultado)
