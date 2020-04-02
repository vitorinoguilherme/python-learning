'''
 sorteioAlunos.py - Dados os nomes dos alunos, sorteia um aluno para apagar o quadro.
 autor: Guilherme Vitorino
 02.04.20 - 15h57min
'''

from random import randint

alunos = []

for i in range(4):
    nome = input("Informe o nome do aluno: ")
    alunos.insert(i, nome)

print(f"Aluno escolhido para apagar quadro: {alunos[randint(0, 3)]}")

