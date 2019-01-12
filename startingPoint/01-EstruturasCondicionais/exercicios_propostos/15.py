""" 15 - Um supermercado deseja reajustar os preços de seus produtos usando o seguinte critério: o produto poderá ter seu preço 
aumentado ou diminuído. Para o preço ser alterado, o produto deve preencher pelo menos um dos requisitos a seguir:

VENDA MÉDIA MENSAL	PREÇO ATUAL	% DE AUMENTO	%DE DIMINUIÇÃO
< 500	< R$ 30,00	10	-
>= 500 e < 1.200	>= R$ 30,00 e < R$ 80,00	15	-
>= 1.200	>= R$ 80,00	-	20

Faça um programa que receba o preço atual e a venda média mensal do produto, calcule e mostre o novo preço.
"""

# DEFINE O VALOR DE AUMENTO E DESCONTO DOS PRODUTOS
aumento_10 = 0.10
aumento_15 = 0.15
desconto_20 = 0.20


valor_atual = int(input("Digite o valor do preço atual do produto: "))
valor_vendam = int(input("Digite o valor da média mensal de venda do produto: "))

if (valor_vendam < 500) or (valor_atual < 30):
    novo_preco = valor_atual + (aumento_10 * valor_atual)

elif((valor_vendam >= 500) and (valor_vendam < 1200)) or ((valor_atual >= 30) and (valor_atual < 80)):
    novo_preco = valor_atual + (aumento15 * valor_atual)

elif(valor_vendam >= 1200) or (valor_atual >= 80):
    novo_preco = valor_atual - (desconto20 * valor_atual) 
        
print("O novo preço será: R$", novo_preco)
    
                            


    

