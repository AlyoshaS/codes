# 7. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((base maior + base menor) * altura) / 2

base_maior, base_menor, altura = [float(x) for x in input("Digite a base maior, a base menor e a altura do trapézio: ").split()]

A = ((base_maior + base_menor) * altura) / 2

print("A área do trapézio é: {0}".format(A))
