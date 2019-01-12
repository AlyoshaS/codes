# 4. Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.

nota1, nota2 = [float(x) for x in input("Digite as duas notas: ").split()]

peso1 = 2
peso2 = 3

mult1 = nota1 * peso1
mult2 = nota2 * peso2
total = peso1 + peso2
media = (mult1 + mult2) / total

print("A média ponderada das notas é: {0}".format(media))
    
