def verifica_primo(n):
   for i in range(2,n):
       if n%i == 0:
           return False 
   return True


def todos_primos(n):
   resposta = []
   for testar in range(2,n+1): #se n=11
       # eu quero a 'lista' [2,3,4...11]
       # preciso escrever range(2,12)
       if verifica_primo(testar):
           resposta.append(testar)
   return resposta
print(todos_primos(10))
