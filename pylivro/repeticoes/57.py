#!/usr/bin/python
# coding: latin-1
# Tabuada quando o usuario insere os numeros desejados

inc = int(input("Digite o primeiro número a imprimir: "))
fim = int(input("Digite o último número a imprimir: "))
y = 2

while inc <= fim:
    print ('2 x %d = %d')% (inc, y)
    inc = inc + 1
    y = 2 * inc
