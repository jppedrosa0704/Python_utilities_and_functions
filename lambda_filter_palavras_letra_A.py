# Use filter para retornar apenas os nomes que começam com a letra A.

nomes = ["Ana", "Bruno", "Amanda", "Carlos", "Arthur"]

comeca_com_a = list(filter(lambda n: n.startswith("A"), nomes))

print(comeca_com_a)
