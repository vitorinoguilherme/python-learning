'''
 tabuada.py - Dado o valor, imprime a tabuada.
 autor: Guilherme Vitorino
 02.04.20 - 13h52min
'''

number = int(input("Informe um valor: "))

print('-'*12)

for i in range(11):
    print(f"{number} x {i:2} = {(number * i):>2}")

print('-'*12)
