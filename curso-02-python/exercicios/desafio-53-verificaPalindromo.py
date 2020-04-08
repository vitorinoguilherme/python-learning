"""
 verificaPalindromo.py - verifica se a frase é um polindromo.
 autor: Guilherme Vitorino
 08.04.20 - 14h26min
"""
# exemplos: apos a sopa; a sacada da casa; a torre da derrota; o lobo ama o lobo


print(f"{' INFORMA SE A FRASE É UM PALÍNDROMO ':=^50}")

frase = str(input("Digite a frase: ")).strip()

frase = frase.split()  # Separa em palavras
frase = ''.join(frase)  # Junta frase sem espaços

inverteFrase = []
for i in range(len(frase) - 1, -1, -1):
    inverteFrase.append(frase[i])
inverteFrase = ''.join(inverteFrase)  # Junta frase invertida sem espaços

if frase == inverteFrase:
    print("\033[1;32mA frase é um PALÍNDROMO! Podemos ler ao contrário e manter o significado.")
else:
    print("\033[1;31mA frase não é um PALÍNDROMO.")
