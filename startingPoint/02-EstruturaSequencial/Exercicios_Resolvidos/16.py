"""
17. Faça um programa que receba o raio, calcule e mostre:

o comprimento de uma esfera; sabe-se que C = 2 * PI * R;
a área de uma esfera; sabe-se que A = PI * R²;
o volume de uma esfera; sabe-se que V = 3/4 * PI * R³
"""

raio = int(input("Informe o raio: "))

comprimento = 2 * 3.14 * raio
area = 3.14 * (raio ** 2)
volume = (4 * 3.14 * (raio ** 3) / 3)

print("O comprimento da esfera será de {0}, a área será de {1} e o volume é {2}.".format(comprimento, area, volume))















