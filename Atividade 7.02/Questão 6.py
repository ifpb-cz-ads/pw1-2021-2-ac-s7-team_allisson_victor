L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
v = int(input("Digite o outro valor a procurar:"))
x = 0
achouP = -1  
achouV = -1
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = x
    if L[x] == v:
        achouV = x
    x += 1
if achouP != -1 and achouV != -1:
    if achouP <= achouV:
        print("Valor 1 foi encontrado antes de Valor 2")
    else:
        print("Valor 2 foi achado antes de Valor 1")