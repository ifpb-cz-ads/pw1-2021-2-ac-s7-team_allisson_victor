primeira = []
segunda = []
aux = ''
while aux != 0:
    n = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if n == 0:
        aux = 0
    else:    
        primeira.append(n)
aux = ''    
while aux != 0:
    n = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if n == 0:
        aux = 0
    else:    
        segunda.append(n)
terceira = primeira[:]
terceira.extend(segunda)
cont = 0
while cont < len(terceira):
    print(terceira[cont])
    cont = cont + 1