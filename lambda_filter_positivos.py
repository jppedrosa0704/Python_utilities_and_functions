#Use filter para retornar apenas os números positivos.

valores = [-5, -2, 0, 3, 7, -1, 9]

valores_positivos = list(filter(lambda p: p > 0, valores))
print(valores_positivos)
