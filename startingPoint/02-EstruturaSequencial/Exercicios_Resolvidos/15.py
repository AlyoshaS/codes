"""
16. Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.
"""

vlr_produto = float(input("Digite o valor do produto: R$"))

desconto = vlr_produto * (10 / 100)
vlr_com_desconto = round(vlr_produto - desconto, 2)

print("O novo valor do produto com desconto será: R$", vlr_com_desconto)















