#!/usr/bin/python
# coding: latin-1
"""
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula 
o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
Entrada: O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade
de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.
Saída: Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da 
igualdade. No caso do salário, também deve haver um espaço em branco após o $.
Exemplo de Entrada 	Exemplo de Saída

25						NUMBER = 25
100						SALARY = U$ 550.00 
5.50
"""
NUMBER = input('')
worked_hours = input('')
value_hours = float(raw_input(''))
SALARY = (worked_hours * value_hours)
print "NUMBER = %d\nSALARY = U$ %.2f" % (NUMBER, SALARY);