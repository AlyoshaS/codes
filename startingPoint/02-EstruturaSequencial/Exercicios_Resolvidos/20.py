"""
22. Faça um programa que receba a medida de dois ângulos de um triângulo, calcule e mostre a medida do terceiro ângulo. Sabe-se que a soma dos ângulos de um triângulo é 180 graus.
"""

angulo1, angulo2 = [int(x) for x in input("Digite a medidas dos dois ângulos do triângulo: ").split()]

angulo3 = 180 - (angulo1 + angulo2)

print("A medida do terceiro ângulo é: ", angulo3, "°")
















