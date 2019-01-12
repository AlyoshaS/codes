""" 21 - Faça um programa que receba:

* O código do estado de origem da carga de um caminhão, supondo que a digitação do código do estado seja sempre válida, ou seja, um número inteiro entre 1 e 5
* O peso da carga do caminhão em toneladas.
* O código da carga, supondo que a digitação do código seja sempre válida, ou seja, um número inteiro entre 10 e 40.

Tabelas:

| CÓDIGO DO ESTADO  | IMPOSTO |
|-------------------|---------|
| 1                 |   35%   |
| 2                 |   25%   |
| 3                 |   15%   |
| 4                 |    5%   |
| 5                 |  Isento |


| CÓDIGO DA CARGA  | PREÇO POR QUILO |
|------------------|-----------------|
| 10 a 20          | 100             |
| 21 a 30          | 250             |
| 31 a 40          | 340             |

Calcule e mostr:

* O peso da carga do caminhão convertido em quilos.
* O preço da carga do caminhão
* O valor do imposto, sabendo-se que o imposto é cobrado sobre o preço da carga do caminhão e depende do estado de origem
* O valor total transportado pelo caminhão, preço da carga mais imposto.
"""

# Entrada de dados:

codigo_estado = int(input("Digite o código do seu estado (entre 1 a 5): "))
peso_carga = int(input("Digite o peso da carga do caminhão em toneladas: "))
codigo_carga = int(input("Digite o código da carga (entre 10 e 40): "))

# Define valor do imposto:

imposto1 = 0.35
imposto2 = 0.25
imposto3 = 0.15 
imposto4 = 0.05
imposto5 = 0

# Define valor do imposto sobre a carga:

if codigo_estado == 1:
	imposto = imposto1

if codigo_estado == 2:
	imposto = imposto2
	
if codigo_estado == 3:
	imposto = imposto3
	
if codigo_estado == 4:
	imposto = imposto4
	
if codigo_estado == 5:
	imposto = imposto5

# Define preço por quilo:

if codigo_carga >= 10 and codigo_carga <= 20:
	preco = 100.00

if codigo_carga >= 21 and codigo_carga <= 30:
	preco = 250.00

if codigo_carga >= 31 and codigo_carga <= 40:
	preco = 340.00

# Define o valor total do imposto e o valor total da carga 

peso_kg = peso_carga * 1000
valor_imposto = preco * imposto
valor_carga = preco + valor_imposto

# Fiz sem olhar o anterior, então fiz de forma diferente o print.
print("- O peso da carga é de {0}KG. \n- O preço da carga é R${1}. \n- O valor total do imposto é R${2}. \n- O valor total da carga é de R${3}.".format(peso_kg, preco, valor_imposto, valor_carga))
