"""
15. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo de um funcionário e o valor de suas vendas,calcule e mostre a comissão e seu salário final.
"""

salario, vlr_vendas = [int(x) for x in input("Digite o valor do seu salário fixo e o valor de suas vendas: ").split()]

comissao = vlr_vendas * (4 / 100)
salario_final = comissao + salario

print("O valor da sua comissão será de R${0} e seu salário final será R${1}.".format(comissao, salario_final))















