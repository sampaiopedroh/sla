cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
naipe = ["o", "c", "p", "e"]

def cria_baralho(naipe, cartas):
    for i in range(len(naipe)):
        for x in range(len(cartas)):
            naipe_atual = naipe[i]
            carta_atual = cartas[x]
            print(naipe_atual+carta_atual)
    return

teste = cria_baralho(naipe, cartas)
