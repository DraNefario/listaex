lista_palavras = ["python", "programação", "lista", "palavra", "longa", "curta"]

mais_longa = max(lista_palavras, key=len)
mais_curta = min(lista_palavras, key=len)

print("Palavra mais longa:", mais_longa)
print("Palavra mais curta:", mais_curta)