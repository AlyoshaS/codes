"""
24. Faça um programa que receba a hora(uma variável para hora e outra para minutos), calcule e mostre:

a hora digitada convertida em minutos;
o total dos minutos, ou seja, os minutos digitados mais a conversão do anterior;
o total dos minutos convertidos em segundos.
"""

hora, minutos = [int(x) for x in input("Digite a hora e os minutos: ").split()]

#conversão

minutos1 = hora * 60
total_min = minutos + minutos1
segundos = total_min * 60

print("{0}h convertida em minutos será {1}, o total de minutos será {2}min e o total em segundos será {3}s".format(hora, minutos1, total_min, segundos)) 
















