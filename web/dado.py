import random

jogador1 = []
jogador2= []

dado = [random.randint(1,6) for i in range(3)]
dado2 = [random.randint(1,6) for i in range(3)]

jogador1 += dado
jogador2 += dado2

soma = sum(jogador1)
soma2 = sum(jogador2)

if soma > soma2:
    print("jogador 1 ganhou")
else:
    print("jogador 2 ganhou")
