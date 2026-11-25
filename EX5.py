list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
llista_nova = []

for x in list_num:
    esta = False
    for y in llista_nova:
        if x == y:
            esta = True
            break
    if not esta:
        llista_nova.append(x)

print("Llista sense duplicats:", llista_nova)