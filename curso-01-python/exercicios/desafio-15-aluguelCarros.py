'''
 aluguelCarros.py - Dados quantidade de dias e km percorridas, calcula preco total.
 autor: Guilherme Vitorino
 02.04.20 - 14h09min
'''

qtdDias = int(input("Informe a quantidade de dias pelo qual o carro foi alugado: "))
qtdKmPercorridos = float(input("Informe a quantidade de Km percorridos: "))

precoTotal = 60.0 * qtdDias + 0.15 * qtdKmPercorridos

print(f"Preço a pagar: R${precoTotal:.2f}")