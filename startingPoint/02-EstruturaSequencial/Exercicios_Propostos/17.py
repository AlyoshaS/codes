#!/usr/bin/python
# coding: latin-1
""" 17 - Pedro comprou um saco de ração com peso em quilos. Ele possui dois gatos, para os quais fornece a quantidade de ração em gramas. 
A quantidade diária de ração fornecida para cada gato é sempre a mesma. Faça um programa que receba o peso do saco de ração e a quantidade
de ração fornecida para cada gato, calcule e mostre quanto restará de ração no saco após cinco dias."""

peso_saco = int(input("Digite o peso do saco de ração: "))
racao_gato1 = int(input("Digite a quantidade de ração para o primeiro gato: "))
racao_gato2 = int(input("Digite a quantidade de ração para o segundo gato: "))

racao_gato1 = racao_gato1 / 1000
racao_gato2 = racao_gato2 / 1000
total_final = peso_saco - 5 * (racao_gato1 + racao_gato2)


print("Após cinco dias sobrará: ", total_final)
