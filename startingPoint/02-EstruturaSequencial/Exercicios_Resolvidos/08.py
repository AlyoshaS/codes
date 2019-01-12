# 9 - Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor) / 2

diag_maior, diag_menor = [float(x) for x in input("Digite a diagonal maior e a diagonal menor do losango: ").split()]

A = (diag_maior * diag_menor) / 2

print("A área do losango é: {0}".format(A))

      

