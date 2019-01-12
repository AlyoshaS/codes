#!/usr/bin/python
# coding: latin-1

# 04 - Faça um programa que receba o salário de um funcionário e o percentual de aumento, calcule e mostre o valor de aumento e novo salário

salario = float(input("Digite o valor do seu salário aqui: "))
perc = int(input("Digite o percentual de aumento: "))

aumento = (salario *(perc / 100))
novo_salario = (salario + aumento)

print("Seu novo salário será: R$", novo_salario)
