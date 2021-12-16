#9) Escreva um programa que lê uma string com uma palavra ou frase, e que gera um dicionário onde 
# cada chave seja um caractere, e seu valor seja a quantidade de vezes que o caractere aparece 
# na frase. Você deve ignorar os espaços em branco.

#Exemplo: "programacao" -> {"p": 1, "r": 2, "o": 2, "g": 1, "a": 2, "m": 1, "c": 1}
frase = input("Digite uma frase para contar as letras:")
d = {}

for l in frase.replace(" ", ""):
    if l in d:
        d[l] = d[l] + 1
    else:
        d[l] = 1
print(d)