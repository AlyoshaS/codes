#!/usr/bin/python
# coding: latin-1
# 23 - Faça um programa que receba o custo de um espetáculo teatral e o preço do convite desse espetáculo. Esse programa deverá calcular
# e mostar a quantidade de convites que devem ser vendidos para que pelo menos o custo do espetáculo seja alcançado

custo = float(input("Digite o custo do espetáculo teatral: "))
convite = float(input("Digite o custo do convite para o espetáculo: "))

qtd = custo / convite
qtd = round(qtd)

print("Deverão ser vendidos", qtd, "convites para que o custo do espetáculo seja alcançado.")
