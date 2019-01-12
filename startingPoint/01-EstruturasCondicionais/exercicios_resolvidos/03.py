# 03 - Faça um programa que receba três números e mostre o maior.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o segundo número: "))

if (numero1 < numero2) and (numero1 > numero3):
	if numero2 < numero3:
		print("A sequência do maior para o menor é: %d, %d e %d." % (numero3, numero2, numero1))
	else:
		print("A sequência do maior para o menor é: %d, %d e %d." % (numero2, numero3, numero1))
		
if (numero2 < numero1) and (numero2 < numero3):
	if numero1 < numero3:
		print("A sequência do maior para o menor é: %d, %d e %d." % (numero3, numero1, numero2))
	else:
		print("A sequência do maior para o menor é: %d, %d e %d." % (numero1, numero3, numero2))
if (numero3 < numero1) and (numero3 < numero2):
	if numero1 < numero2:
		print("A sequência do maior para o menor é: %d, %d e %d." % (numero2, numero1, numero3))
	else:
		print("A sequência do maior para o menor é: %d, %d e %d." % (numero1, numero2, numero3))
	
