"""
05 - Faça um programa que receba dois números e execute uma das operações listadas a seguir, de acordo com a escolha do 
usuário. Se foi digitada uma opção inválida, mostre mensagem de erro e termine a execução do programa. As opções são:

  1. O primeiro número elevado ao segundo número.
  2. Raiz quadrada de cada um dos números.
  3. Raiz cúbida de cada um dos números.
"""
from math import sqrt, pow

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo número: "))
print("\n")
print("+---------------------+----------------------------------------------+")
print("|      Opções:        |                Operação:                     |")
print("|---------------------|----------------------------------------------|")
print("|         1           | O primeiro número elevado ao segundo número. |")
print("|         2           | Raiz quadrada de cada um dos números.        |")
print("|         3           | Raiz cúbida de cada um dos números.          |")
print("+---------------------+----------------------------------------------+")
print("\n")
operacao = int(input("Digite a operação desejada de acordo com a lista acima: "))

if operacao == 1:
	print("O resultado do número %d elevado ao número %d é %d!" % (numero1, numero2, pow(numero1, numero2)))

if operacao == 2:
        print("A raiz quadrada de %d é %.2f e a raiz quadrada de %d é %.2f" % (numero1, sqrt(numero1), numero2, sqrt(numero2)))
              
if operacao == 3:
	print("A raiz cúbica de %d é %.2f e a raiz cúbica de %d é %.2f" % (numero1, pow(numero1, 1/3.0), numero2, pow(numero2, 1/3.0)))


