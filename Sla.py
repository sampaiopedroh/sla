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

# Carro mais caro
carros = ['Up', 'Uno', 'Celtinha', 'Kombi', 'Kwid']
valores = [10, 5, 1000000, 100, 50]


def carro_caro(precos):
    j = 0
    caro = precos[j]
    for i in range(len(precos)):
        if precos[i] > caro:
            caro = precos[i]
            j = i
        else:
            caro = caro
    print(f'O carro mais caro é: {carros[j]}\n'
          f'Ele custa: R${precos[j]}')


carro_caro(valores)

# Separador de pares e impares
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares = []
# imps = []
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         pares.append(nums[i])
#         continue
#     imps.append(nums[i])
#
#
# print(nums)
# print(pares)
# print(imps)


# Lista professores
# profs = ['Cordeiro', 'Danilo', 'Lucas Silva', 'Lucas Demetrius', 'Jones', 'Ana Claúdia', 'Caio']
# materias = ['SW & TX', 'Python', 'Front-end', 'Edge', 'Calculo', 'ST & Emp', 'Web']
# for i in range(len(profs)):
#     print(f'O(a) prof {profs[i]} leciona : {materias[i]}')


# Peça ao usuário um professor de input, verifique se esse professor está na lista.
# Se estiver, busque o local do professor na lista, print o que o professor escolhido leciona.
# Caso contráio, mande ele digitar novamente
# profs = ['Cordeiro', 'Danilo', 'Lucas Silva', 'Lucas Demetrius', 'Jones', 'Ana Claúdia', 'Caio']
# materias = ['SW & TX', 'Python', 'Front-end', 'Edge', 'Calculo', 'ST & Emp', 'Web']
# escolha = input('Diga o nome do professor que procura:\n-> ')
# while not(escolha in profs):
#     print(f"Não encotramos o '{escolha}', tente novamente")
#     escolha = input('Diga o nome do professor que procura:\n-> ')
#
# for i in range(len(profs)):
#     if escolha == profs[i]:
#         print(f'O(a) prof {profs[i]} leciona : {materias[i]}')


# Achar o carro mais caro
# carros = ['Up', 'Uno', 'Celtinha', 'Gol', 'Fusca']
# precos = [10, 5, 1000000, 100, 5000]
# ano = [2015, 2001, 2014, 2010, 1970]
# indice_do_mais_caro = 0
# mais_caro = precos[indice_do_mais_caro]
#
# for i in range(len(precos)):
#     if precos[i] > mais_caro:
#         mais_caro = precos[i]
#         indice_do_mais_caro = i
# print(f'O carro mais caro é: {carros[indice_do_mais_caro]};\n'
#       f'Seu ano de fabricação é: {ano[indice_do_mais_caro]};\n'
#       f'Ele custa: R${precos[indice_do_mais_caro]:.2f}')


# Procurar um carro
# carros = ['Up', 'Uno', 'Celtinha', 'Gol', 'Fusca']
# precos = [10, 5, 1000000, 100, 5000]
# ano = [2015, 2001, 2014, 2010, 1970]
# frase_erro = ', '.join(carros)
#
# print(f'As opções são: {frase_erro}.')
# escolha = input('Qual carro você quer ver ?\n-> ')
# while escolha not in carros:
#     print(f'Opção inválida !!!\nOpções válidas: {frase_erro}.\n')
#     escolha = input('Qual carro você quer ver ?\n-> ')
#
# indice_do_mais_caro = 0
# mais_caro = precos[indice_do_mais_caro]
#
# for i in range(len(precos)):
#     if precos[i] > mais_caro:
#         mais_caro = precos[i]
#         indice_do_mais_caro = i
# print(f'O carro escolhido é: {carros[indice_do_mais_caro]};\n'
#       f'Seu ano de fabricação é: {ano[indice_do_mais_caro]};\n'
#       f'Ele custa: R${precos[indice_do_mais_caro]:.2f}')


# Começando funções
# Antes:
# qnt = input(f'Diga a quantidade de garrafas: ')
# while not qnt.isnumeric():
#     print('Errso\nDiga uma opção válida')
#     qnt = input(f'Diga a quantidade de garrafas: ')
#
# idade = input(f'Diga a sua idade: ')
# while not idade.isnumeric():
#     print('Errso\nDiga uma opção válida')
#     idade = input(f'Diga a sua idade: ')

# Depois:
# def verifica_numero(msg_pergunta, msg_de_erro):
#     num = input(msg_pergunta)
#     while not num.isnumeric():
#         print('Erro')
#         num = input(msg_de_erro)
#     return int(num)
#
#
# a = verifica_numero('Diga a quantidade de garrafas:\n-> ', 'Diga uma quantidade válida:\n-> ')
# print(f'Quantidade de guarrafas selecionadas: {a}')
# b = verifica_numero('Diga a sua idade:\n-> ', 'Diga uma idade válida:\n-> ')
# print(f'Sua idade é: {b}')


# Procurar algo (com def)
# def procura_nome(lista_de_opcoes, msg, msg_de_erro, msg_de_acerto):
#     teste = input(msg)
#     while not(teste in lista_de_opcoes):
#         teste = input(msg_de_erro)
#
#     for i in range(len(lista_de_opcoes)):
#         if teste == lista_de_opcoes[i]:
#             print(msg_de_acerto + teste)
#     return teste
#
#
# a = procura_nome(['Ana', 'Bia', 'Caio'], 'Diga o nome de um aluno:\n-> ', 'Não achamos este aluno\nTente com outro nome:\n-> ', f'Escontramos o aluno: ')


# Função que procura um indice
# def procura_indice(lista, msg, msg_erro):
#     elemento_teste = input(msg)
#     indice = 0
#     while elemento_teste not in lista:
#         elemento_teste = input(msg_erro)
#     for i in range(len(lista)):
#         if elemento_teste == lista[i]:
#             indice = i
#             break
#     print(f"O elemento {elemento_teste} esta na lista no indice: {indice}.\n")
#     return indice
#
#
# a = procura_indice(['1', '2', '3', '4'], 'Diga um número:\n-> ', 'Escolha outro número:\n-> ')
#
# b = procura_indice(['a', 'b', 'c', 'd'], 'Diga uma letra:\n-> ', 'Escolha outra letra:\n-> ')

# Acha o maior (com def)
# def verifica_maior_ou_menor(msg, lista):
#     maior_ou_menor = input(msg)
#     indice = 0
#     teste = lista[indice]
#     if maior_ou_menor == '>':
#         for i in range(len(lista)):
#             if lista[i] > teste:
#                 teste = lista[i]
#                 indice = i
#         print(f'O maior elemento é: {teste}')
#
#     elif maior_ou_menor == '<':
#         for i in range(len(lista)):
#             if lista[i] < teste:
#                 teste = lista[i]
#                 indice = i
#         print(f'O menor elemento é: {teste}')
#     return indice
#
#
# a = verifica_maior_ou_menor("Você quer saber o menor ou maior ? ('<' ou '>')\n-> ", [1, 2, 3, 4])

# # Inverte uma lista (com def)
# def inverte_lista(lista):
#     ultimo = len(lista) - 1
#     for i in range(len(lista)//2):
#         aux = lista[i]
#         lista[i] = lista[(ultimo - i)]
#         lista[(ultimo - i)] = aux
#     print(lista)
#
#
# inverte_lista([1, 2, 3, 4])
# inverte_lista([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


