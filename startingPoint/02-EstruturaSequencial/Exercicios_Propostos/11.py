#!/usr/bin/python
# coding: latin-1

# 11 - Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro

num1 = int(input("Digite o primeiro número positivo: "))
num2 = int(input("Digite o segundo número positivo: "))

r = num1 ** num2
r1 = num2 ** num1

print ("O primeiro número elevado ao segundo número é: ", r, "\nO segundo número elevado ao primeiro número é: ", r1)
