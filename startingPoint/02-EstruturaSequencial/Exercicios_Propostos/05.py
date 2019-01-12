#!/usr/bin/python
# coding: latin-1

# 05 - Faça um programa que receba o salário base de um funcionário, calcule e mostre o salário a receber, sabendo-se que o funcionário
# tem gratificação de 5% sobre o salário base e paga imposto de 7% sobre este salário.

sal_base = float(input("Digite o valor do seu salário aqui: "))

grat = sal_base * 5 / 100
imp = sal_base * 7 / 100

sal_receber = (sal_base + grat - imp)

print("Seu salário será: R$", sal_receber)
