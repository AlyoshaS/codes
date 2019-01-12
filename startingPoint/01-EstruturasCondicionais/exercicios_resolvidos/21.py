"""
21 - Faça um programa que receba a idade e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual grupo de risco 
essa pessoa se encaixa.

<img src="http://i.imgur.com/UeR94ww.png" />
"""
idade = int(input("Digite sua idade: "))
peso =  float(input("Digite seu peso: "))

if idade < 20:
	if peso < 60:
		print("Você pertence ao grupo de risco 9.")
	elif peso <= 90:
		print("Você pertence ao grupo de risco 8.")
	else:
		print("Você pertence ao grupo de risco 7.")
elif idade <= 50:
	if peso < 60:
		print("Você pertence ao grupo de risco 6.")
	elif peso <= 90:
		print("Você pertence ao grupo de risco 5.")
	else:
		print("Você pertence ao grupo de risco 4.")
else:
	if peso < 60:
		print("Você pertence ao grupo de risco 3.")
	elif peso <= 90:
		print("Você pertence ao grupo de risco 2.")
	else:
		print("Você pertence ao grupo de risco 1.")
