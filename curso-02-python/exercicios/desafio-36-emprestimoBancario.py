"""
 emprestimoBancario.py - Calcula valor da prestação e válida empréstimo.
 autor: Guilherme Vitorino
 07.04.20 - 21h59min
"""
cores = {'limpa':'\033[m', 'negrito':'\033[1m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}

valorCasa = float(input("Informe o valor da casa: R$ "))
salario = float(input("Informe o seu salário: R$ "))
anos = int(input("Quantos anos vai pagar a casa: R$ "))

prestacaoMensal = valorCasa / (anos * 12)

if prestacaoMensal > (salario * 0.3):
    print(f"{cores['negrito']}Seu emprestimo foi negado, prestação mensal é {prestacaoMensal:.2f} excede 30% do salário.")
else:
    print(f"{cores['negrito']}Seu emprestimo foi efetivado, a prestação mensal é R$ {prestacaoMensal:.2f}")