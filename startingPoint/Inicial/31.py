#Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: √a² + b². Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através
#da equação. Imprima o resultado dessa operação.

a = int(input("Digite aqui o primeiro cateto: "))
b = int(input("Digite aqui o segundo cateto: "))

A = a ** 2
B = b ** 2
soma = (A + B)
hipotenusa = (soma ** (1/2.0))

print("A hipotenusa é: ", hipotenusa)








     
