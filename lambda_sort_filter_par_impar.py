import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},

]

produtos_novos = copy.deepcopy(produtos)

produtos_novos.sort(key=lambda p: p['nome'])
for p in produtos_novos:
    p['preco'] = round(p['preco'] * 1.10, 2)

print()
print('lista antiga')
print(*produtos, sep='\n')
print()
print(*produtos_novos, sep='\n')

print('lista de produtos pares')

pares = list(filter(lambda p: p['preco'] % 2 == 0, produtos ))
print(pares)
