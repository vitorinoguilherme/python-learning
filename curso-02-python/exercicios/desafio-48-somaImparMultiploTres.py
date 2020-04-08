"""
 somaImparMultiploTres.py - Soma dos números ímpares dos múltiplos de três [1-500].
 autor: Guilherme Vitorino
 08.04.20 - 13h07min
"""
print(f"{' Soma dos números ímpares dos múltiplos de três [1-500] ':=^70}")

soma = 0
for numeroImpar in range(1, 500):
    if numeroImpar % 2 != 0 and numeroImpar % 3 == 0:
        soma += numeroImpar

print(f"Soma = {numeroImpar}")