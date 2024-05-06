# carros = ['Up', 'Gol', 'Celta', 'Kombi', 'Uno']
# precos = [10, 20, 1000, 15, 5]
# indice = 0
# maisCaro = precos[indice]
# for i in range(1, len(precos)):
#     if precos[i] > maisCaro:
#         maisCaro = precos[i]
#         indice = i
# print(f'O carro mais caro é o {carros[indice]}, no valor de: R${maisCaro:.2f} reais')

# lista = [3, 4, 5, 6, 7, 8, 9]
# ultimo = len(lista) - 1
# tam = len(lista) // 2
# for i in range(tam):
#     aux = lista[i]
#     lista[i] = lista[(ultimo - i)]
#     lista[ultimo - i] = aux
# print(lista)

# def par(num):
#     if num % 2 == 0:
#         print(f'{num} é par')
#     else:
#         print(f'{num} não é par')
#     return
# par(3)

# def testa_vogal(letra):
#     vogal = ['a', 'e', 'i', 'o', 'u']
#     if letra in vogal:
#         print(f'{letra} é uma vogal')
#     else:
#         print(f'{letra} não é uma vogal')
#     return
# testa_vogal('a')

# def testa_vogal_2(letra):
#     resposta = f'{letra} não é uma vogal'
#     vogal = ['a', 'e', 'i', 'o', 'u']
#     if letra in vogal:
#         resposta = f'{letra} é uma vogal'
#         return resposta
#     return resposta
# testa_vogal_2('e')

# def calcula_soma(lista):
#     soma = 0
#     for i in range(len(lista)):
#         soma += lista[i]
#     print(f'A média dos elementos da lista deu: {soma}')
#     return
# sla = [1, 2, 3]
# calcula_soma(sla)

# def calcula_media(lista):
#     media = 0
#     for i in range(len(lista)):
#         media += lista[i]
#     media /= len(lista)
#     print(f'A média dos elementos da lista deu: {media}')
#     return
# sla = [1, 2, 3]
# calcula_media(sla)

# def conta_vogais(frase):
#     vogais = ['a', 'e', 'i', 'o', 'u']
#     qnt_vogais = 0
#     for i in range(len(frase)):
#         if frase[i] in vogais:
#             qnt_vogais += 1
#     print(f'Na sua frase/palavra, há {qnt_vogais} vogais')
#     return
# conta_vogais('pedro')

# def conta_pares(lista):
#     pares = 0
#     lista_pares = []
#     for i in range(len(lista)):
#         if lista[i] % 2 == 0:
#             pares += 1
#             lista_pares.append(lista[i])
#     print(f'Nessa lista há {pares} números pares\nSendo eles: {lista_pares}')
#     return
# sla = [1, 2, 3, 4, 5, 6]
# conta_pares(sla)

# def verifica_se_num(num):
#     while not num.isnumeric():
#         print('Não é um número')
#         num = input('Tente novamente:\n-> ')
#     return
#
#
# sla = input('Diga um número:\n-> ')
# verifica_se_num(sla)


# vinhos = ['vinho_1', 'vinho_2', 'vinho_3']
# precos = [10, 20, 30]
# opcoes_validas = [0, 1, 2]
#
#
# def verifica(opcao):
#     while (not opcao.isnumeric) and (not opcao in opcoes_validas):
#         print('Opção inválida')
#         opcao = input('Tente novamente:\n-> ')
#     return opcao
#
#
# def vinho_escolhido(indice):
#     indice = opcao
#     for i in range(len(vinhos)):
#         if vinhos[i] == opcao:
#             indice = i
#             return indice
#     return indice
#
#
# print(f'Temos {len(opcoes_validas)} opções de vinhos:\n'
#       f'1 - {vinhos[0]}\n'
#       f'2 - {vinhos[1]}\n'
#       f'3 - {vinhos[2]}\n')
#
# escolha = input('Escolha uma opção de vinho:\n-> ')
# verifica(escolha)
# vinho_escolhido()
# print(f'Você escolheu o vinho: {vinhos[indice]}\n'
#       f'Que custa: R${precos[indice]}')

lista_nome = ['Ana', 'Bia', 'Caio', 'Dani']


def verifica_nome(lista, nome):
    for i in range(len(lista)):
        if nome in lista[i]:
            return True
    return False


pergunta = input('Diga seu nome:\n-> ')
verifica_nome(lista_nome, pergunta)

