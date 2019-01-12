"""
18. Sabe-se que, para iluminar de maneira correta os cômodos de uma casa, para cada m² deve-se usar 18 W de potência. Faça um programa que receba as duas dimensões de
um cômodo(em metros), calcule e mostre a sua área(em m²) e a potência de iluminação que deverá ser utilizada.
"""

largura, comprimento = [int(x) for x in input("Digite a largura e o comprimento do cômodo: ").split()]

area = largura * comprimento
potencia = area / 18

print("A área do cômodo é {0}m² e a potência de iluminação que deverá ser utilizada é de {1}w".format(area, potencia))
















