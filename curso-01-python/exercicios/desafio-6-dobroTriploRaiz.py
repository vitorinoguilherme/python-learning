'''
 dobroTriploRaiz.py - calcula o dobro, triplo e raiz do número.
 autor: Guilherme Vitorino
 02.04.20 - 13h42min
'''

number = int(input("Informe o número: "))

print(f"O dobro [{number}]: {2 * number}\n"
      f"O triplo [{number}]: {3 * number}\n"
      f"A raiz quadrada [{number}]: {number**(1/2):.2f}")