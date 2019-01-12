"""7 - Faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.

Menu de opções:

Somar dois números
Raiz Quadrada de um número.
Digite a opção desejada
"""
from math import sqrt
print("Menu", "\n1 - Somar dois números", "\n2 - Raiz quadrada de um número")
op = int(input("Digite sua opção: "))

if(op == 1):
    num1 = int(input("Digite o valor para o primeiro número: "))
    num2 = int(input("Digite o valor para o segundo número: "))
    soma = num1 + num2
    print("A soma de", num1, "e", num2, "é", soma)

if(op == 2):
    num1 = int(input("Digite um valor "))
    raiz = sqrt(num1)
    print("A raiz quadrada de", num1, "é", raiz)

if(op != 1) and (op != 2):
    print("Opção inválida!")
          
            
    
