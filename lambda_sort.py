# Use sort() com lambda para ordenar os alunos da maior para a menor nota.

# Depois, imprima a lista ordenada mostrando apenas o nome e a nota.
import copy


# alunos_ordenados = alunos.sort(key=lambda n: n['nota'])

def ordenar():
    alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 7.2},
    {"nome": "Beatriz", "nota": 9.1},
    {"nome": "Daniel", "nota": 6.8}
]
    for p in alunos:
        ordenados = sorted(alunos, p['nota'])
    print(*ordenados)