"""
 verificaMaioridade.py - Verifica se é maior ou menor de idade.
 autor: Guilherme Vitorino
 08.04.20 - 14h28min
"""
from datetime import date

anoAtual = date.today().year

numMaiorIdade = 0
numMenorIdade = 0
for num in range(0, 7):
    anoNascimento = int(input("Informe o ano de nascimento: "))
    if anoAtual - anoNascimento < 18:
        numMenorIdade += 1
    elif anoAtual - anoNascimento >= 18:
        numMaiorIdade += 1

print(f"\033[31m{numMenorIdade} pessoas não atingiram a maioridade!")
print(f"\033[33m{numMaiorIdade} pessoas já são maiores")
