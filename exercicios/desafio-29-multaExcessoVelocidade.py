"""
 multaExcessoVelocidade.py - Indica se o motorista foi multado ou não
 autor: Guilherme Vitorino
 04.04.20 - 21h30min
"""

velocidade = float(input("Digite a velocidade do carro: km/h "))
precoMulta = 7.0    # por cada km

if velocidade > 80.0:
    print(f"Você está acima do limite, foi multado!")
    print(f"Valor da multa: R$ {((velocidade - 80) * precoMulta):.2f}")
else:
    print("Parabéns, você é um ótimo motorista.")
