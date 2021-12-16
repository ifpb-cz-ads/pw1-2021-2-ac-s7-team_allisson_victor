T = [-10, -8, 0, 1, 2, 5, -2, -4]
Maior = T[0] 
Menor = T[0]
TMedia = 0
for x in T:
    if x < Maior:
        Menor = x
    if x > Maior:
        Maior = x
    TMedia = TMedia + x
print(f"Temperatura máxima: {Maior} °C")
print(f"Temperatura mínima: {Menor} °C")
print(f"Temperatura média: {TMedia / len(T)} °C")