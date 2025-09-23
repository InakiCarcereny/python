lista = [1, 2, 3, 2, 4, 1, 5, 3, 6]

unicos = []

[unicos.append(x) for x in lista if x not in unicos]

print(unicos)