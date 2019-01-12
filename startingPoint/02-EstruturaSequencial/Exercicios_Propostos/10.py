#!/usr/bin/python
# coding: latin-1
""" 11 - Faça um programa que receba um número positivo e maior que zero, calcule e mostre:
- o número digitado ao quadrado;
- o número digitado ao cubo;
- a raiz quadrada do número digitado;
- a raiz cúbica do número digitado;
"""

num = int(input("Digite um número positivo: "))

quad = num ** 2
cubo = num ** 3
r2 = num ** (1/2.0)
r3 = num ** (1/3.0)

r2 = round(r2, 2)
r3 = round(r3, 2)

print ("O quadrado será: ", quad, "\nO cubo será: ", cubo, "\nA raiz quadrada será: ", r2, "\nA raiz cubica será: ", r3)
