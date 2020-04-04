'''
 digitosSeparados.py - Dado o número separa digitos.
 autor: Guilherme Vitorino
 04.04.20 - 17h15min
'''

numero = int(input("Informe um número: "))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

if numero < 0 or numero > 9999:
    print(f"O número deve estar entre 0-9999")
else:
    print(f"Unidade: {u}\n"
          f"Dezena:  {d}\n"
          f"Centena: {c}\n"
          f"Milhar:  {m}\n")

