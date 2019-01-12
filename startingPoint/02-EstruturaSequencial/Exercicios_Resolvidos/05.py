# 6. Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.


peso = float(input("Digite seu peso em quilogramas: "))

peso_gramas = round(peso * 1000)

print("Seu peso em gramas é: {0} gramas".format(peso_gramas))
