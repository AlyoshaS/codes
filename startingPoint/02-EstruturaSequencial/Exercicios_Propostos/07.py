#!/usr/bin/python
# coding: latin-1

# 07 - Faça um programa que receba o valor de um depósito e o valor da taxa de juros, calcule
#e mostre o valor do rendimento e o valor total depois do rendimento

dep = float(input("Digite o valor do depósito aqui: "))
taxa = float(input("Digite o valor da taxa de juros: "))

rend = dep * taxa / 100

total = (dep + rend)

print("O valor do rendimento será: R$", rend, "O valor total após o rendimento será: R$", total)
