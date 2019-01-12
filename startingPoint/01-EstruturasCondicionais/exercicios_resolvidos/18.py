"""
18 - Faça um programa que receba a altura e o sexo de uma pessoa; calcule e mostre seu peso ideal, utilizando as seguintes fórmulas
(onde h é a altura):
  * para homens: (72.7 * h) - 58.
  * para mulheres: (62.1 * h) - 44.7.
"""
height = float(input("Digite a sua altura: "))
sex = input("Digite o seu sexo(M para mulher ou H para homem): ")

if sex == 'M':
	print("O peso ideal para mulheres com altura %.2fm é de %.2fKg." % (height, ((62.1 * height) - 44.7)))
elif sex == 'H':
	print("O peso ideal para homens com altura %.2fm é de %.2fKg." % (height, ((72.7 * height) - 58)))
else:
	print("Opção incorreta!")
