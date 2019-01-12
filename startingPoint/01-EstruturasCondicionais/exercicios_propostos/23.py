"""23 - Faça um programa que receba o preço, o tipo(A - alimentação, L - limpeza e V - vestuário) e a 
refrigeração(S - produto que necessita de refrigeração e N - produto que não necessita de refrigeração) de um produto.
Suponha que haverá apenas a digitação de **dados válidos** e, quando houver digitação de letras, utilize maiúsculas. 
Calcule e mostre:

* O valor adicional, de acordo com a tabela a seguir.

<img src="http://i.imgur.com/GpssyIC.png" />

* O valor do imposto, de acordo com a regra a seguir.

| PREÇO                | PERCENTUAL SOBRE O PREÇO   |
|----------------------|----------------------------|
| < R$ 25,00           | 5%                         |
| >= R$ 25,00          | 8%                         |


* O preço de custo, ou seja, preço mais imposto.

* O desconto, de acordo com a regra a seguir.
O produto que **não** preencher nenhum dos requisitos abaixo terá desconto de 3% , caso contrário, 0(zero). Os requisitos são: <br />
**Tipo:** A <br />
**Refrigeração:** S
* O novo preço, ou seja, preço de custo mais adicional menos desconto.

* A classificação, de acordo com a regra a seguir.

| NOVO PREÇO                    | CLASSIFICAÇÃO              |
|-------------------------------|----------------------------|
| <= R$ 50,00                   | Barato                     |
| Entre R$ 50,00 e R$ 100,00    | Normal                     |
| >= R$ 100,00                  | Caro                       |
"""
# Recebe os dados do usuário:
preco = int(input("Digite o preço do produto: "))
tipo = input("Digite o tipo do produto(A - alimentação, L - limpeza e V - vestuário): ")
refrigeracao = input("Digite o tipo de refrigeração (S - necessita de refrigeração, N - não necessita de refrigeração): ")

# Define valor adicional dos produtos de acordo com o tipo de refrigeracao:
if refrigeracao == 'N':
		if tipo == 'A':
				if preco < 15:
						adicional = 2
				else:
						adicional = 5
		if tipo == 'L':
				if preco < 10:
						adicional = 1.50
				else:
						adicional = 2.50
		if tipo == 'V':
				if preco < 30:
						adicional = 3
				else:
						adicional = 2.50
else:
		if tipo == 'A':
				adicional = 8
		if tipo == 'L':
			adicional = 0
		if tipo == 'V':
			adicional = 0
print("O valor adicional do produto é de R$", adicional)

# Define o imposto:
if preco < 25.00:
		imposto = preco * .05
		preco_custo = preco + imposto
		print("O preço de custo será {0} e o valor do imposto {1}".format(preco_custo, imposto))
else:
		imposto = preco * .08
		preco_custo = preco + imposto
		print("O preço de custo será {0} e o valor do imposto {1}".format(preco_custo, imposto))

# Define o desconto:
if(tipo != 'A') and (refrigeracao != 'S'):
		desconto = round(preco_custo * .03, 2)
		novo_preco = preco_custo + adicional - desconto
		print("Este produto tem desconto de {0} e o novo preço é de R${1}.".format(desconto, novo_preco))
		
else:
		desconto = 0
		novo_preco = preco_custo + adicional - desconto
		print("Este produto não possui desconto!")

# Define a classificacao de preco:
if novo_preco <= 50:
		print("Classificação: Barato!")
elif novo_preco > 50 and novo_preco < 100:
		print("Classificação: Normal!")
else:
		print("Classificação: Caro!")