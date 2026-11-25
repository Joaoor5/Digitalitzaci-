
#Ejercicio 4

list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

maximo = list_num[0]
minimo = list_num[0]

for num in list_num:
    if num > maximo:
        maximo = num  
        
    if num < minimo:
        minimo = num  

print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)
