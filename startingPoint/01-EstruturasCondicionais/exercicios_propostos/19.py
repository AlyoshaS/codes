"""19 - Faça um programa que receba:

O código de um produto comprado, supondo que a digitação do código do produto seja sempre válida, ou seja, um número inteiro 
entre 1 e 10. O peso do produto em quilos.
O código do país de origem, supondo que a digitação do código seja sempre válida, ou seja, um número inteiro entre 1 e 3
Tabelas:

CÓDIGO DO PAÍS DE ORIGEM	IMPOSTO
1	                           0%
2	                          15%
3	                          25%
CÓDIGO DO PRODUTO	PREÇO POR GRAMA
1 a 4	                      10
5 a 7	                      25
8 a 10	                      35
Calcule e mostre:

O peso do produto convertido em gramas.
O preço total do produto comprado.
O valor do imposto, sabendo-se que ele é cobrado sobre o preço total do produto e depende do país de origem.
O valor total, preço total do produto mais imposto
"""

# Recebe o código do produto comprado, o peso em KG e o código do país de origem.

codigo_produto = int(input("Digite o código do produto (1 a 10): "))
pesoKG = int(input("Digite o peso do produto em quilogramas: "))
codigo_pais = int(input("Digite o código do país de origem do produto(1 a 3): "))

# Define o peso do produto convertido em gramas.

peso_gramas = pesoKG * 1000
print("O peso em gramas será: ", peso_gramas)

# Define o preço total do produto comprado.

if(codigo_produto >= 1) and (codigo_produto <= 4):
    preco_grama = 10

if(codigo_produto >= 5) and (codigo_produto <= 7):
    preco_grama = 25

if(codigo_produto >= 8) and (codigo_produto <= 10):
    preco_grama = 35

preco_total = peso_gramas * preco_grama
print("O preço total do produto é: R$", preco_total)

# Define o valor do imposto.

if(codigo_pais == 1):
    imposto = 0

if(codigo_pais == 2):
    imposto = preco_total * 0.15

if(codigo_pais == 3):
    imposto = preco_total * 0.25

valor_total = imposto + preco_total
print("O preço total do produto, incluindo o imposto, é: R$", valor_total)
