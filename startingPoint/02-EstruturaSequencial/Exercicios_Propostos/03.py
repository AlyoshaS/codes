#!/usr/bin/python
# coding: latin-1

# 03 - Faça um programa que receba o salário de um funcionário, calcule e mostre o novo salário, sabendo-se que este sofreu um aumento de 25%

salario = int(input("Digite o valor do seu salário aqui: "))

aumento = (25 *(salario / 100))
novo_salario = (salario + aumento)

print("Seu novo salário será: ", novo_salario)
