"""
12 - Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação.

**TABELA 1 - PERCENTUAL DE AUMENTO**

| PREÇO                         | %                                    |
|-------------------------------|--------------------------------------|
| Até R$ 50,00                  | 5                                    |
| Entre R$ 50,00 e R$ 100,00     | 10                                   |
| Acima de R$ 100,00            | 15                                   |

**TABELA 2 - CLASSIFICAÇÕES**

| NOVO PREÇO                             | CLASSIFICAÇÃO                        |
|----------------------------------------|--------------------------------------|
| Até R$ 80,00                           | Barato                               |
| Entre R$ 80,00 e R$ 120,00(inclusive)  | Normal                               |
| Entre R$ 120,00 e R$ 200,00(inclusive) | Caro                                 |
| Maior que R$ 200,00                    | Muito caro                           |
"""
preco = float(input("Digite o preço do produto: "))

# Percentual de aumento:
if preco < 50:
	print("O novo preço é: R$%.2f." %(preco + (preco * 0.05)))
elif preco < 100:
	print("O novo preço é: R$%.2f." %(preco + (preco * 0.10)))
else:
	print("O novo preço é: R$%.2f." %(preco + (preco * 0.15)))

# Classificação conforme a tabela:
if preco < 80:
	print("Classificação: Barato.")
elif preco <= 120:
	print("Classificação: Normal.")
elif preco <= 200:
	print("Classificação: Caro.")
else:
	print("Classificação: Muito caro.")
