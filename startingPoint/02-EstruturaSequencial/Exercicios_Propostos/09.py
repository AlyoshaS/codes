#!/usr/bin/python
# coding: latin-1

# 09 - Faça um programa que calcule e mostre a área de um círculo. Sabe-se que: Área = PI * R²

raio = float(input("Digite aqui o raio do círculo: "))

PI = 3.1415

area = (PI * raio**2)
area = round(area, 2)

print("A área será de: ", area)
