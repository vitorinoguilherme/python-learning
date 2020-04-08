"""
 numerosPares.py - Mostra números pares no intervalo entre 1 e 50.
 autor: Guilherme Vitorino
 08.04.20 - 13h
"""
print(f"{' Números pares, intervalo entre 1 e 50 ':=^70}")

for numeroPar in range(1, 51):
    if numeroPar % 2 == 0:
        print(numeroPar, end=' ')