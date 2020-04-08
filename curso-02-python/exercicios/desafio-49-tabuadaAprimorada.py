'''
 tabuadaAprimorada.py - Dado o valor, imprime a tabuada.
 autor: Guilherme Vitorino
 08.04.20 - 13h16min
'''

print(f"{' IMPRIME A TABUADA ':=^40}")
number = int(input("Informe um valor: "))

print('-'*20)

for i in range(0, 11):
    print(f"{number} x {i:2} = {(number * i):>2}")

print('-'*20)