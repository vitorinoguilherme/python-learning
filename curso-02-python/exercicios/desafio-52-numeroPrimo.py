'''
 numeroPrimo.py - Indica se o número é ou não PRIMO.
 autor: Guilherme Vitorino
 08.04.20 - 16h25min
'''

print(f"{' INFORMA SE O NÚMERO É PRIMO ':=^40}")

numero = int(input("Informe um número: "))
total = 0

for count in range(1, numero + 1):
    if numero % count == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{count} ', end='')

print(f'\n\033[mO número {numero} foi divisível {total} vezes')

if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')