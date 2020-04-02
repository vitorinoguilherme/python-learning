'''
 precoComDesconto.py - Dado o preço informa o preço com desconto.
 autor: Guilherme Vitorino
 02.04.20 - 14h
'''

precoProduto = float(input("Informe o preço do produto: R$"))
desconto = 0.05

print(f"\nPreço do produto: R$ {precoProduto:.2f}\n"
      f"Preço do produto com desconto: R${(precoProduto - precoProduto * desconto):.2f}")