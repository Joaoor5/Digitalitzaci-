 # Ordena una llista de números de menor a major.
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
for i in range(len(list_num)):
    for j in range(i + 1, len(list_num)):
        if list_num[i] > list_num[j]:
            list_num[i], list_num[j] = list_num[j], list_num[i]
print(list_num)
