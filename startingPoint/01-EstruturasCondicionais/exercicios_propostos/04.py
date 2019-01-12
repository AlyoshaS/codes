""" 4. Faça um programa que receba três números obrigatoriamente em ordem crescente e um quarto número que não siga essa regra, 
Mostre, em seguida, os quatro números em ordem decrescente. Suponha que o usuário digitará quatro números diferentes.
"""
n1, n2, n3 = [int(x) for x in input("Digite três números em ordem crescente: ").split()]
n4 = int(input("Digite o número (fora de ordem): "))

if n4 > n3:
    print("a ordem decrescente é: {0} - {1} - {2} - {3}".format(n4, n3, n2, n1))

if n4 > n2 and n4 < n3:
    print("a ordem decrescente é: {0} - {1} - {2} - {3}".format(n3, n4, n2, n1))

if n4 > n1 and n4 < n2:
    print("a ordem decrescente é: {0} - {1} - {2} - {3}".format(n3, n2, n4, n1))

if n4 < n1:
    print("a ordem decrescente é: {0} - {1} - {2} - {3}".format(n3, n2, n1, n4))
    
              
