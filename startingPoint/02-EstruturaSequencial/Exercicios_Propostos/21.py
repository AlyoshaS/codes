#!/usr/bin/python
# coding: latin-1
"""21 - Faça um programa que receba um número real, calcule e mostre:
- a parte inteira desse número;
- a parte fracionária desse número;
- o arredondamento desse número"""

num = float(input("Digite o numero: "))

i = int(num)
f = num - i
a = round(num)

print("A parte inteira desse número: ", i, "\nA parte fracionária desse número: ", f, "\nO arredondamento desse número: ", a)
