"""17 - Dados três valores X, Y e Z, verifique se eles podem ser os comprimentos dos lados de um triângulo e, se forem, 
verifique se é um triângulo equilátero, isóceles ou escaleno. Se eles não formarem um triângulo, escreva uma mensagem. 
Considere que:

- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
- Chama-se equilátero o triângulo que tem três lados iguais.
- Denomina-se isóceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

# RECEBE x, y, E z DO USUARIO

x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

# DEFINE SE E UM TRIANGULO

if(x < y + z) and (y < x + z) and (z < x + y):
    if((x == y) and (y == z)):
        print("Triângulo Equilátero")
    elif((x == y) or (x == z) or (y == z)):
        print("Triângulo Isóceles")
    elif((x != y) and (x != z) and (y != z)):
        print("Triângulo Escaleno")

else:
    print("Essas medidas não formam um triângulo")
