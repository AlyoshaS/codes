# 3.Faça um programa que receba três números e mostre-os em ordem crescente. Suponha que o usuário digitará três números diferentes.

n1 = int(input("Digite o primeiro número: "))       
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if num1 < num2 and num1 < num3 :
        if num2 < num3 :
                print("A ordem crescente é: {0} - {1} - {2}".format (num1, num2, num3))
        else:
                print("A ordem crescente é: {0} - {1} - {2}".format (num1, num3, num2))
        
if num2 < num1 and num2 < num3 :
        if num1 < num3 :
                print("A ordem crescente é: {0} - {1} - {2}".format (num2, num1, num3))
        else:
                print("A ordem crescente é: {0} - {1} - {2}".format (num2, num3, num1))


if num3 < num1 and num3 < num2 :
        if num1 < num2 :
                print("A ordem crescente é: {0} - {1} - {2}".format (num3, num1, num2))
        else:
                print("A ordem crescente é: {0} - {1} - {2}".format (num3, num2, num1))
    
