list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
llista_invertida = []

# Recorrem la llista des de l'últim índex fins al primer
for i in range(len(list_num) - 1, -1, -1):
    llista_invertida.append(list_num[i])

print(llista_invertida)
# Resultat: [10, 6, 9, 3, 8, 1, 5, 4, 7, 2]
