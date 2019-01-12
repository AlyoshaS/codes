#!/usr/bin/python
# coding: latin-1

"""12 - Sabe-se que: 1 pé = 12 polegadas; 1 jarda = 3 pés; 1 milha = 1.760 jardas. Faça um programa que receba a medida em pés, 
faça as conversões a seguir e mostre os resultados.
- polegadas
- jardas
- milhas
"""

pes = int(input("Digite a medida: "))

polegadas = pes * 12
jarda = pes * 3
milha = pes * 1760

print("A medida em polegadas é: ", polegadas, "\nA medida em jardas é: ", jarda, "\nA medida em milhas é: ", milha)
