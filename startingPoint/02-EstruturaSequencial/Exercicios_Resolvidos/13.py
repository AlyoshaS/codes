"""
14. Faça um programa que receba o valor dos catetos de um triângulo, calcule e mostre o valor da hipotenusa.
"""

cat_oposto, cat_adjacente = [float(x) for x in input("Digite o valor do cateto oposto e o valor do cateto adjacente: ").split()]

hipotenusa = (cat_oposto ** 2) + (cat_adjacente ** 2)
hipotenusa = hipotenusa ** (1/2.0)

print("O valor da hipotenusa: ", hipotenusa)















