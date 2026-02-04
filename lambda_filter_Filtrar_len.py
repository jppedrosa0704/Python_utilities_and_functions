#Filtre apenas as palavras que possuem mais de 4 letras.
palavras = ["python", "java", "c", "javascript", "go"]

maior_4_letras = list(filter(lambda k: len(k) > 4, palavras))
print(maior_4_letras)