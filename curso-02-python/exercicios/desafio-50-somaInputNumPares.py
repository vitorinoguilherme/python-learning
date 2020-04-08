'''
 somaInputNumPares.py - Dado 6 valores, soma somente pares.
 autor: Guilherme Vitorino
 08.04.20 - 13h21min
'''

print(f"{' SOMA NÚMEROS PARES ':=^40}")

valores = []
soma = 0
for indice in range(0, 6):
    numero = int(input(f"Informe o {indice+1}º número inteiro: "))
    if numero % 2 == 0:
        soma += numero
        valores.append(numero)

print(f"Valores PARES digitados {valores}. A SOMA = {soma}")
