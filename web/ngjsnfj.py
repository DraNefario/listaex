import random

alfabeto = list("abcdefghijklmnopqrstuvwxyz")

random.shuffle(alfabeto)

letra = random.choice(alfabeto)

palpite = input(f"Adivinhe a posição da letra '{letra}': ")

posicao_correta = alfabeto.index(letra) + 1 
if int(palpite) == posicao_correta:
    print("Parabéns! Você acertou a posição.")
else:
    print(f"Infelizmente, você errou. A posição correta era {posicao_correta}.")
