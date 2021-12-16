conta = input("Digite a sequência de parênteses a validar:")
n = 0
pilha = []
while n < len(conta):
    if conta[n] == "(":
        pilha.append("(")
    if conta[n] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")
    n = n + 1
if len(pilha) == 0:
    print("Conta escrita corretamente")
else:
    print("A conta está escrita de forma errada!")