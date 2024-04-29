# nums = []
# cal = 0
# tam = input('Diga o tamanho da lista:\n-> ')
# while not tam.isnumeric():
#     print('Opção inválida')
#     tam = input('Diga o tamanho da lista:\n-> ')
# tam = int(tam)
#
# for i in range(tam):
#     num = input(f'Diga o {i + 1}° número:\n-> ')
#     while not num.isnumeric():
#         print('Opção inválida')
#         num = input(f'Diga o {i + 1}° número:\n-> ')
#     num = int(num)
#     nums.append(num)
#
# for i in range(len(nums))
#     cal += nums[i]
# cal /= len(nums)
# print(f'A média dos {tam} números é: {cal}')


# nums = []
# tam = input('Diga o tamanho da lista:\n-> ')
# while not tam.isnumeric():
#     print('Opção inválida')
#     tam = input('Diga o tamanho da lista:\n-> ')
# tam = int(tam)
#
# for i in range(tam):
#     num = input(f'Diga o {i + 1}° número:\n-> ')
#     while not num.isnumeric():
#         print('Opção inválida')
#         num = input(f'Diga o {i + 1}° número:\n-> ')
#     num = int(num)
#     nums.append(num)
#
# maior = nums[0]
# for i in range(len(nums)):
#     if nums[i] > maior:
#         maior = nums[i]
#     else:
#         maior = maior
# print(f'O maior número é: {maior}')


# carros = ['Up', 'Uno', 'Celtinha', 'Kombi', 'Kwid']
# precos = [10, 5, 1000000, 100, 50]
# j = 0
# caro = precos[j]
#
# for i in range(len(precos)):
#     if precos[i] > caro:
#         caro = precos[i]
#         j = i
#     else:
#         caro = caro
# print(f'O carro mais caro é: {carros[j]}\n'
#       f'Ele custa: R${precos[j]}')


carros = ['Up', 'Uno', 'Celtinha', 'Kombi', 'Kwid']
precos = [10, 5, 1000000, 100, 50]

frase_erro = ', '.join(carros)

print(f'As opções são: {frase_erro}.')
escolha = input('Qual carro você quer ver ?\n-> ')
while escolha not in carros:
    print(f'Opção inválida !!!\nOpções válidas: {frase_erro}.\n')
    escolha = input('Qual carro você quer ver ?\n-> ')

j = 0
for i in range(len(carros)):
    if escolha == carros[i]:
        j = i
        break
        
print(f'O valor do {escolha} é: R${precos[j]}')


