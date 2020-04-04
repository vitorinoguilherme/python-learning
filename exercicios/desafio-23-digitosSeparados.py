'''
 digitosSeparados.py - Dado o número separa digitos.
 autor: Guilherme Vitorino
 04.04.20 - 17h15min
'''

numero = int(input("Informe um número: "))

if( numero < 0 or numero > 9999 ):
    print(f"O número deve estar entre 0-9999")
else:
    numero = str(numero)
    print(f"Unidade: {numero[3]}\n"
          f"Dezena:  {numero[2]}\n"
          f"Centena: {numero[1]}\n"
          f"Milhar:  {numero[0]}\n")