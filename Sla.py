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

# Função para calucular idade
# def calcula_ideade(ano_nascimento):
#     cal_idade = 2024 - ano_nascimento
#     return cal_idade
#
#
# nome = input("Diga seu nome:\n-> ")
# ano = int(input("Diga em que ano você nasceu:\n-> "))
# ano = calcula_ideade(ano)
# print(f"\n{nome}, você tem {ano} anos ")

# Número maior
# def maior_num(lista):
#     teste_maior = lista[0]
#     for i in range(1, (len(lista))):
#         if teste_maior < lista[i]:
#             teste_maior = lista[i]
#     return teste_maior
#
#
# sla = [1, 2, 3, 4]
# maior = maior_num(sla)
# print(f"O maior número é o: {maior}")
#
# sla2 = [5, 56, 5464, 31321]
# maior = maior_num(sla2)
# print(f"O maior número é o: {maior}")

# Proximo minuto
# def prox_min(h, minu):
#     if minu >= 59 and h >= 23:
#         minu = 0
#         h = 0
#         return f"O próximo minuto é: 0{h}:0{minu}"
#     elif minu >= 59:
#         if h < 10:
#             return f"O próximo minuto é: 0{h}:0{minu}"
#         minu = 0
#         h += 1
#         return f"O próximo minuto é: {h}:0{minu}"
#     else:
#         minu += 1
#         if h < 10 and minu < 10:
#             return f"O próximo minuto é: 0{h}:0{minu}"
#         elif h < 10:
#             return f"O próximo minuto é: 0{h}:{minu}"
#         elif minu < 10:
#             return f"O próximo minuto é: {h}:0{minu}"
#         return f"O próximo minuto é: {h}:{minu}"
#
#
# hora = int(input("Diga que horas são:\n-> "))
# while not (0 <= hora < 24):
#     hora = int(input("Diga que horas são:\n-> "))
#
# minuto = int(input("Diga que minutos são:\n-> "))
# while not(0 <= minuto < 60):
#     minuto = int(input("Diga que minutos são:\n-> "))
#
# proximo_minuto = prox_min(hora, minuto)
# print(proximo_minuto)

# verifica se é número
# def verifica_num(num):
#     while not num.isnumeric():
#         num = input("Diga um valor válido:\n-> ")
#     num = int(num)
#     print(f"O número escolhido foi {num}")
#
#
# numero = input("Diga um número:\n-> ")
# verifica_num(numero)

# numero de telefone
# def valida_telefone(num):
#     while (not num.isnumeric()) or (not (len(num) in [8, 9, 11])):
#         num = input("Diga um número válido:\n-> ")
#     return num
#
#
# telefone = input("Diga seu número de telefone:\n-> ")
# teste = valida_telefone(telefone)
# print(f"Seu telefone é: {teste}")

# valida carros
# carros = ['Up', 'Uno', 'Celtinha', 'Kombi', 'Kwid']
# precos = [10, 5, 1000000, 100, 50]
#
# frase = ', '.join(carros)
#
# print(f'As opções são: {frase}.')
# escolha = input('Qual carro você quer ver ?\n-> ')
# while escolha not in carros:
#     print(f'Opção inválida !!!\nOpções válidas: {frase}.\n')
#     escolha = input('Qual carro você quer ver ?\n-> ')
#
# j = 0
# for i in range(len(carros)):
#     if escolha == carros[i]:
#         j = i
#         break
#
# print(f'O valor do {escolha} é: R${precos[j]}')

# verifica ímpar
# def verifica_impar(lista):
#     imp = 0
#     for i in range(len(lista)):
#         if lista[i] % 2 != 0:
#             imp += 1
#     print(f"Nessa lista há {imp} ímpares e {len(lista) - imp} pares")
#     return
# 
# 
# sla = [1, 2, 3, 4]
# verifica_impar(sla)

