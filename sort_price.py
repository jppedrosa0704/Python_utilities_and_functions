#Sort dictionarys by price

price = [
    {"nome": "teclado", "preco": 150},
    {"nome": "mouse", "preco": 80},
    {"nome": "monitor", "preco": 900}
]

price.sort(key=lambda p: p['preco'])
print(*price, sep='\n')