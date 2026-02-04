# Use filter e lambda para criar uma nova lista contendo apenas os números pares.

numeros = [1,2,3,4,5,6,7,8,9,10]

# numeros_pares = copy.deepcopy(numeros)

numeros_pares = list(filter(lambda p: p % 2 == 0, numeros))
print(numeros_pares)

numeros_impares = list(filter(lambda i: i % 2 != 0, numeros ))
print(numeros_impares)