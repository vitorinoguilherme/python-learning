'''
 calculosParede.py - Dado a largura e altura informa área e qtd litros de tinta.
 autor: Guilherme Vitorino
 02.04.20 - 13h57min
'''

largura = float(input("Informe a largura (m): "))
altura = float(input("Informe a altura (m): "))

area = largura * altura
qtdTinta = area / 2.0

print(f"\nÁrea da parede em metros quadrados: {area:.2f}(m²)\n"
      f"Quantidade de tinta em litros: {qtdTinta:.2f}(l)")