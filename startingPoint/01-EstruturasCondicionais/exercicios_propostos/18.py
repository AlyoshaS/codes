"""18 - Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre a cassificação dessa pessoa.

+------------------+------------------------------------------------------+
|                  |                       PESO                           |
|    ALTURA        +------------------------------------------------------+
|                  | Até 60      Entre 60 e 90(inclusive)    Acima de 90  |
+------------------+------------------------------------------------------+
|Menores que 1,20  |   A                     D                     G      |
|De 1,20 a 1,70    |   B                     E                     H      |
|Maiores que 1,70  |   C                     F                     I      |
+------------------+------------------------------------------------------+
"""

# Recebe altura e peso do usuario:

altura = float(input("Digite a altura: "))
peso = float(input("Digite o peso: "))

# Define a classificacao:

if(altura < 1.20):
    if(peso <= 60):
        print("A")
    if(peso > 60) and (peso <= 90):
        print("D")
    if(peso > 90):
        print("G")

if(altura >= 1.20) and (altura <= 1.70):
    if(peso <= 60):
        print("B")
    if(peso > 60) and (peso <= 90):
        print("E")
    if(peso > 90):
        print("H")

if(altura > 1.70):
    if(peso <= 60):
        print("C")
    if(peso > 60) and (peso <= 90):
        print("F")
    if(peso > 90):
        print("I")
