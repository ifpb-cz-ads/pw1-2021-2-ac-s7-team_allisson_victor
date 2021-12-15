#3) Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

lista1 = []
lista2 = []
while True:
    x = int(input("Digite um numero para a primeira lista (0 para terminar):"))
    if x == 0:
        break
    lista1.append(x)
while True:
    x = int(input("Digite um numero para a segunda lista (0 para terminar):"))
    if x == 0:
        break
    lista2.append(x)

lista3 = []
misturar_tudo = lista1[:]
misturar_tudo.extend(lista2)
x = 0
while x < len(misturar_tudo):
    y = 0
    while y < len(lista3):
        if misturar_tudo[x] == lista3[y]:
            break
        y = y + 1
    if y == len(lista3):
        lista3.append(misturar_tudo[x])
    x = x + 1
x = 0
while x < len(lista3):
    print("Posição "f"{x}: {lista3[x]}")
    x = x + 1