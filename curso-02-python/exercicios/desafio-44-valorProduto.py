"""
 valorProduto.py - Calcula valor do produto de acordo com a condição de pagamento.
 autor: Guilherme Vitorino
 07.04.20 - 20h48min
"""
cores = {'limpa': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'magenta': '\033[1;35m',
         'azul': '\033[1;34m'}

precoProd = float(input("Informe o preço normal do produto: R$ "))
print('-'*45)
print(f"1 - À vista {cores['azul']}dinheiro/cheque: 10%{cores['limpa']} de desconto.\n"
      f"2 - À vista {cores['azul']}cartão: 5%{cores['limpa']} de desconto.\n"
      f"3 - Em até {cores['azul']}2x no cartão:{cores['limpa']} preco normal.\n"
      f"4 - {cores['azul']}3x ou mais{cores['limpa']} no cartão:"
      f" {cores['azul']}20%{cores['limpa']} de juros.""")
print('-'*45)
condicaoPagamento = int(input("Escolha a condição do pagamento -> "))

if condicaoPagamento == 1:
    print(f"Preço a pagar ={cores['verde']} R$ {(precoProd - precoProd * 0.1):.2f}")
elif condicaoPagamento == 2:
    print(f"Preço a pagar ={cores['verde']} R$ {(precoProd - precoProd * 0.05):.2f}")
elif condicaoPagamento == 3:
    print(f"Preço a pagar ={cores['verde']} R$ {precoProd:.2f}")
elif condicaoPagamento == 4:
    print(f"Preço a pagar ={cores['verde']} R$ {(1.20 * precoProd):.2f}")
