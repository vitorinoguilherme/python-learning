'''
 aumentoSalario.py - Dado o salário informa o salário com aumento.
 autor: Guilherme Vitorino
 02.04.20 - 14h03min
'''

salario = float(input("Informe o salário: "))
aumento = 0.15

print(f"Salário funcionário: R$ {salario:.2f}\n"
      f"Salário com aumento: R$ {(salario + salario * aumento):.2f}")