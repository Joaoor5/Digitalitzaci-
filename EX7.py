# Uneix dues llistes en una sola.
list_num = [2, 7, 4, 5, 1]
list_num2 = [ 8, 3, 9, 6, 10]
llista_invertida = []
for i in range(len(list_num) - 1, -1, -1):
    llista_invertida.append(list_num[i])
for i in range(len(list_num2) - 1, -1, -1):
    llista_invertida.append(list_num2[i])
print(llista_invertida)
