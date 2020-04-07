"""
 comparaNumeros.py - Compara se os numeros são iguais ou qual é o maior.
 autor: Guilherme Vitorino
 07.04.20 - 19h29min
"""

primeiroNumero = float(input("Informe o primeiro numero: "))
segundoNumero = float(input("Informe o segundo numero: "))

if primeiroNumero > segundoNumero:
    print(f"O primeiro valor {primeiroNumero:.2f}, é maior que o segundo {segundoNumero:.2f}")
elif segundoNumero > primeiroNumero:
    print(f"O segundo valor {segundoNumero:.2f}, é maior que o primeiro {primeiroNumero:.2f}")
else:
    print(f"Não existe valor maior, os dois são iguais!")
