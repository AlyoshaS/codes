#!/usr/bin/python
# coding: latin-1

''' Contagem regressiva do lançamentp de um foguete. O programa deverá imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela '''

x = 10
while x != 0:
    print (x)
    x = x - 1
    if x == 0:
        print ("0 e Fogo!")
