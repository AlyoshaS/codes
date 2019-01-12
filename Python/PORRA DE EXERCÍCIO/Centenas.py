# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

numero = input("Digite um numero menor que 1000: ")
qt_numero = len(numero)

if qt_numero == 3:
    centena = numero [0 : 1]
    dezena = numero [1 : 2]
    unidade = numero [2 : 3]
    print("Centena", centena, ", dezena ", dezena, "e unidade ", unidade)

if qt_numero == 2:
    dezena = numero [0 : 1]
    unidade = numero [1 : 2]
    print("Dezena ", dezena, "e unidade ", unidade)

if qt_numero == 1:
    unidade = numero [0 : 1]
    print(unidade, "unidades.")
