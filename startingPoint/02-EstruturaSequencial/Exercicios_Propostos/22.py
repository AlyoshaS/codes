#!/usr/bin/python
# coding: latin-1
# 22 - Faça um programa que receba uma hora formada por hora e minutos(um número real), calcule e mostre a hora digitada apenas em minutos.
#Lembre-se de que: para quatro e meia, deve-se digitar 4.30; os minutos vão de 0 a 59.

hora = float(input("Digite a hora: "))

h = int(hora)
m = hora - h
conversao = (h * 60) + (m * 100)

print("Em minutos a hora digitada será: ", conversao)
