"""
08 - Um banco concederá um crédito especial aos seus clientes, de acordo com o saldo médio no último ano. Faça um programa 
que receba o saldo médio de um cliente e calcule o valor de crédito, de acordo com a tabela a seguir. Mostre o saldo médio 
e o valor do crédito.

| SALDO MÉDIO                   | PERCENTUAL                           |
|-------------------------------|--------------------------------------|
| Acima de R$ 400,00            | 30% do saldo médio                   |
| R$ 400,00 *----° R$ 300,00    | 25% do saldo médio                   |
| R$ 300,00 *----° R$ 200,00    | 20% do saldo médio                   |
| Até R$ 200,00                 | 10% do saldo médio                   |
"""
saldo_medio = float(input("Digite o saldo médio do último ano: "))

if saldo_medio > 400:
	print("De acordo com o saldo médio de R$ %.2f do ano anterior, o valor de crédito será R$ %.2f." % (saldo_medio, (saldo_medio*0.30)))
elif saldo_medio >= 300:
	print("De acordo com o saldo médio de R$ %.2f do ano anterior, o valor de crédito será R$ %.2f." % (saldo_medio, (saldo_medio*0.25)))
elif saldo_medio >= 200:
	print("De acordo com o saldo médio de R$ %.2f do ano anterior, o valor de crédito será R$ %.2f." % (saldo_medio, (saldo_medio*0.20)))
else:
	print("De acordo com o saldo médio de R$ %.2f do ano anterior, o valor de crédito será R$ %.2f." % (saldo_medio, (saldo_medio*0.10)))
