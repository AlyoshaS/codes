# 02 - Faça um programa que receba dois números e mostre o menor.
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 < numero2:
	print("O número {0} é menor que o número {1}.".format(numero1, numero2))
if numero2 < numero1:
	print("O número {0} é menor que o número {1}.".format(numero2, numero1))

