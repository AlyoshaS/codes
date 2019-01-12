#!/usr/bin/python
# coding: latin-1

# 06 - Faça um programa que receba o salário base de um funcionário, calcule e mostre o seu salário a receber, sabendo-se que o funcionário
# tem gratificação de R$50 e paga imposto de 10% sobre o salário base

sal_base = float(input("Digite o valor do seu salário aqui: "))

grat = 50
imp = sal_base * 10 / 100

sal_receber = (sal_base + grat - imp)

print("O salário a receber será: R$", sal_receber)
