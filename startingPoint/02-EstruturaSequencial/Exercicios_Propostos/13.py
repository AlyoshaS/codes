#!/usr/bin/python
# coding: latin-1

"""13 - Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
- a idade da pessoa
- quantos anos ela terá em 2050"""

ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade_atual = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento

print("A sua idade atual é: ", idade_atual, "\nA sua idade em 2050 será: ", idade_2050)
