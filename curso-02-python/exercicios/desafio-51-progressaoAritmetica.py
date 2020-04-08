'''
 progressaoAritmetica.py - Mostra progressão aritmética.
 autor: Guilherme Vitorino
 08.04.20 - 13h30min
'''

print(f"{' PROGRESSÃO ARITMÉTICA - PA ':=^40}")

primeiroTermo = float(input("Informe o primeiro termo da PA: "))
razao = float(input("Informe a razão da PA: "))


for i in range(0,10):
    print(f"{(i+1):2}º Termo: {(primeiroTermo + (razao * i)):.2f}")