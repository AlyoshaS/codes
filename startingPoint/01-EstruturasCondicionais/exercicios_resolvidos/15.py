"""
15 - Uma empresa decide aplicar descontos nos seus preços usando a tabela a seguir. Faça um programa que receba o preço atual de um produto e seu
código e que calcule e mostre o valor de desconto e o novo preço.

| PREÇO ATUAL                | % DE DESCONTO   |
|----------------------------|-----------------|
| Até R$ 30,00               | Sem desconto    |
| Entre R$ 30,00 e R$ 100,00 | 10%             |
| Acima de R$ 100,00         | 15%             |
"""
preco = float(input("Digite o valor atual do produto: "))
codigo = int(input("Digite o código do produto: "))

if preco < 30:
	print("Este produto, código %d, não possui desconto. O preço continuará R$%.2f." % (codigo, preco))
elif preco <= 100:
	print("Este produto, código %d, possui desconto de R%.2f. O novo preço é R$%.2f." % (codigo, (preco * 0.10), (preco - (preco * 0.10))))
else:
	print("Este produto, código %d, possui desconto de R%.2f. O novo preço é R$%.2f." % (codigo, (preco * 0.15), (preco - (preco * 0.15))))


