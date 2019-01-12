#!/usr/bin/python
# coding: latin-1
#20 - Sabe-se que o quilowatt de energia custa um quinto do salário mínimo. Faça um programa que receba o valor do salário mínimo e a
#quantidade de quilowatts consumida por uma residência, calcule e mostre:

vlr_sal = int(input("Digite o valor do salário mínimo: "))
qtd_kw = int(input("Digite quantidade de quilowatt: "))

vlr_kw = vlr_sal / 5
vlr_reais = vlr_kw * qtd_kw
desc = (vlr_reais * 15) / 100
vlr_desc = vlr_reais - 100

vlr_kw = round(vlr_kw, 2)
vlr_reais = round(vlr_reais, 2)
vlr_desc = round(vlr_desc, 2)

print("O valor do quilowatt é: ", vlr_kw, "\nO valor a ser pago por essa residência é: R$", vlr_reais, "\nO valor a ser pago com desconto de 15% é: R$", vlr_desc)
