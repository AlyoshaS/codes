#!/usr/bin/python
# coding: latin-1
# Tabuada de 2

fim = int(input("Digite o último número a imprimir: "))
x = 1
y = 2

while x <= fim:
    print ('2 x %d = %d')% (x, y)
    x = x + 1
    y = 2 * x
    
