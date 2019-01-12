#!/usr/bin/python
# coding: latin-1

n = int(input("Digite o primeiro número: "))
n1 = int(input("Digite o segundo número: "))
x = 1
contador = 0

while x <= n1:
    contador = contador + n
    x = x + 1
print ("%d / %d = %d")% (n, n1, contador)
