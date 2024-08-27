def verif_pali(string):
    pos_ult = len(string) - 1
    ult = string[pos_ult]
    pos_pri = 0
    pri = string[pos_pri]
    for i in range(len(string)//2):
        if pri == ult:
            pos_ult -= 1
            pos_pri +=1
        else:
            return False
    return True

teste = verif_pali("aba")
teste_II = verif_pali("abcba")
print(teste, teste_II)
