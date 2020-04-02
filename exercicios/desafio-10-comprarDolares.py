'''
 comprarDolares.py - Dado o valor na conta, mostra quantos dólares é possível comprar.
 autor: Guilherme Vitorino
 02.04.20 - 13h55min
'''

account = float(input("Digite o valor na conta: R$"))
conversaoDolar = 3.27

print(f"\nCom o valor da conta R${account:.2f} é possível comprar: US${(account / conversaoDolar):.2f}")