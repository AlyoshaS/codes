#!/usr/bin/python
# coding: latin-1
# 19 - Faça um programa que receba a medida do ângulo formado por uma escada apoiada no chão e econstada na parede e a altura da parede onde
#está a ponta da escada, calcule e mostre a medida desta escada.

import math
ang = int(input("Digite o ângulo formado pela escada apoiada ao chão e encontada na parede: "))
alt = int(input("Digite a altura da parede onde está a ponta da escada: "))

radiano = ang * 3.14 / 180
escada = alt / math.sin(radiano)

escada = round(escada, 2)

print("A altura da escada é: ", escada)
