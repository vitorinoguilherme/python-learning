'''
 apresentacaoAlunos.py - Dado o ângulo cálcula seno, cosseno e tangente.
 autor: Guilherme Vitorino
 02.04.20 - 17h06min
'''

from random import randint

alunos = []

for i in range(4):
    nome = input("Informe o nome do aluno: ")
    alunos.insert(randint(0, 3), nome)

print("Ordem de sorteação das apresentações.")
for i in range(4):
    print(f"{i} - {alunos[i]}")
