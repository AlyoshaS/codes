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

"""
NAO USA ACENTO EM COMENTARIO! ISSO PODE DAR MERDA
"""

# Recebe os dados do usuario
preco = float(input("Digite o preço do produto: "))
tipo = input("Digite o tipo do produto(A - alimentação, L - limpeza e V - vestuário): ")
refrigeracao = input("Digite o tipo de refrigeração (S - necessita de refrigeração, N - não necessita de refrigeração): ")

# Obtem e exibe o valor adicional
#--------------------------------------------------------------------------------------------------------------------------------
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
    if tipo == 'L' or tipo == 'V':
        adicional = 0

print("O valor adicional do produto é de R$ %.2f" % (adicional))
#--------------------------------------------------------------------------------------------------------------------------------



# Obtem e exibe o valor do imposto e o preco de custo
#--------------------------------------------------------------------------------------------------------------------------------
if preco < 25.00:
    imposto = preco * .05
else:
    imposto = preco * .08

preco_custo = preco + imposto
print("Valor do imposto %.2f\nPreco de custo %.2f " % (imposto, preco_custo))
#--------------------------------------------------------------------------------------------------------------------------------



# Obtem desconto e exibe o novo preco
#--------------------------------------------------------------------------------------------------------------------------------
if(tipo != 'A') and (refrigeracao != 'S'):
    novo_preco = preco_custo + adicional - preco_custo * .03
    print("Novo preco: %.2f" % (novo_preco))
else:
    print("Não possui desconto")

#--------------------------------------------------------------------------------------------------------------------------------



# Exibe a classificacao do produto
#--------------------------------------------------------------------------------------------------------------------------------
if novo_preco <= 50:
    print("Classificação: Barato!")
elif novo_preco > 50 and novo_preco < 100:
    print("Classificação: Normal!")
else:
    print("Classificação: Caro!")
