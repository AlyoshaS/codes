#!/usr/bin/python
# coding: latin-1

"""14 - O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos
aplicados ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, o percentual de lucro do distribuidor e
o percentual de impostos, calcule e mostre:
- o valor correspondente ao lucro do distribuidor;
- o valor correspondente aos impostos;
- o preço final do veículo."""

p_fab = int(input("Digite o preço de fábrica: "))
perc_d = int(input("Digite o percentual de lucro do distribuidor: "))
perc_i = int(input("Digite o percentual de impostos: "))

vlr_d = (p_fab * perc_d) / 100
vlr_i = (p_fab * perc_i) / 100
p_final = p_fab + vlr_d + vlr_i

print("o valor correspondente ao lucro do distribuidor é: R$", vlr_d, "\nO valor correspondente aos impostos é: R$", vlr_i, "\nO preço final do veículo é: R$)", p_final)
