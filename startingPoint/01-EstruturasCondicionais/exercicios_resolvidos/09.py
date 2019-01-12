"""
09 - O preço, ao consumidor, de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e com os impostos,
ambos aplicados ao custo de fábrica. As porcentagens encontram-se na tabela a seguir. Faça um programa que receba o custo de 
fábrica de um carro e mostre o preço ao consumidor.

| CUSTO DE FÁBRICA                  | % DO DISTRIBUIDOR                    | % DOS IMPOSTOS                       |
|-----------------------------------|--------------------------------------|--------------------------------------|
| Até R$ 12.000,00                  | 5                                    | isento                               |
| Entre R$ 12.000,00 e R$ 25.000,00 | 10                                   | 15                                   |
| Acima de R$ 25.000,00             | 15                                   | 20                                   |
"""
custo_fabrica = float(input("Digite o custo de fábrica: "))

if custo_fabrica <= 12000:
	print("O valor do carro é R$%.2f." % (custo_fabrica + (custo_fabrica * 0.05)))
elif custo_fabrica <= 25000:
	print("O valor do carro é R$%.2f." % (custo_fabrica + (custo_fabrica * 0.10) + (custo_fabrica * 0.15)))
else:
	print("O valor do carro é R$%.2f." % (custo_fabrica + (custo_fabrica * 0.15) + (custo_fabrica * 0.20)))
