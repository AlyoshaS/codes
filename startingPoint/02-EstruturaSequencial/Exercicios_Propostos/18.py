#!/usr/bin/python
# coding: latin-1
""" 18 - Cada degrau de uma escada tem X de altura. Faça um programa que receba essa altura e a altura que o usuário deseja alcançar
subindo a escada, calcule e mostre quantos degraus ele deverá subir para atingir seus objetivo, sem se preocupar com a altura do usuário.
Todas as medidas fornecidas devem estar em metros."""

a_degrau = int(input("Digite a altura da escada: "))
a_usuario = int(input("Digite a altura que você deseja chegar: "))

qtd_degraus = a_usuario / a_degrau


print("Você deverá subir: ", qtd_degraus, "degraus")
