'''
 tiposPrimitivos.py - avalia tipos e formatações.
 autor: Guilherme Vitorino
 02.04.20 - 13h37min
'''

var = input("Digite algo: ")

print("O tipo primitivo desse valor é ", type(var))
print("Só tem espaços? ", var.isspace())
print("É número? ", var.isnumeric())
print("É alfabético? ", var.isalpha())
print("É alfanumérico? ", var.isalnum())
print("Está em maiúsculas? ", var.isupper())
print("Está em minúsculas? ", var.islower())
print("Está capitalizada? ", var.istitle())




