#!/usr/bin/python
# coding: latin-1

# 02 - Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada dessas notas

nota1 = int(input("Digite a primeira nota: "))
peso1 = int(input("Digite o peso da primeira nota: "))

nota2 = int(input("Digite a segunta nota: "))
peso2 = int(input("Digite o peso da segunda nota: "))

nota3 = int(input("Digite a terceira nota: "))
peso3 = int(input("Digite o peso da terceira nota: "))

soma1 = nota1 * peso1
soma2 = nota2 * peso2
soma3 = nota3 * peso3
total = peso1 + peso2 + peso3
media = (soma1 + soma2 + soma3) / total

print(media)
