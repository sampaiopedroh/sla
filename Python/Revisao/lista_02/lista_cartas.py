cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
naipe = ["o", "c", "p", "e"]

def lista_cartas(naipe):
    for i in range(len(cartas)):
        carta_naipe = cartas[i] + naipe
        print(carta_naipe)
    return

teste = lista_cartas(naipe[1])
