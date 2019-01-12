# 5. Faça um programa que receba o peso de uma pessoa, calcule e mostre:
# o novo peso, se a pessoa engordar 15% sobre o peso digitado;
# o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.

peso = float(input("Digite seu peso atual: "))

peso15 = (peso * 15 / 100) + peso
peso20 = (peso - (peso * 20) / 100)

print("Se você engordar 15% do seu peso, seu peso será: {0}. Caso emagreça 20%, seu peso será: {1}".format(peso15, peso20))
