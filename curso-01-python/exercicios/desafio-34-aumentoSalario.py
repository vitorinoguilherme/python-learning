"""
 aumentoSalario.py - Calcula aumento do salário de acordo com o salário vigente.
 autor: Guilherme Vitorino
 04.04.20 - 22h14min
"""
salarioFuncionario = float(input("Digite o salário: R$ "))


if salarioFuncionario > 1250.00:
    # Aumento de 10% salario > 1250
    print(f"Salario com aumento: {(1.1 * salarioFuncionario):.2f}")
else:
    # Aumento de 15% salario <= 1250
    print(f"Salario com aumento: {(1.15 * salarioFuncionario):.2f}")