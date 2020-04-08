"""
 baseConversao.py - Dado um numero converte para uma base escolhida.
 autor: Guilherme Vitorino
 07.04.20 - 19h21min
"""

numero = int(input("Informe um número inteiro: "))

print("-=" * 20)
print('''Escolha uma das bases de conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
print("-=" * 20)

opc = int(input("Escolha uma opção -> "))

if opc == 1:
    print(f"O número em binário é {bin(numero)}")
elif opc == 2:
    print(f"O número em octal é {oct(numero)}")
elif opc == 3:
    print(f"O número em hexadecimal é {hex(numero)}")
else:
    print("Opção inválida!")




