# 8 - Faça um programa que mostre a data e a hora do sistema nos seguintes formatos DD/MM/AAAA - mês por extenso e hora:minuto

import time

d = strftime("%d")
mes = strftime("%m")
mes = int(mes)
ano =  strftime("%Y")
print("Data atual: {0}/{1}/{2}".format(d,mes,ano))

if(mes == 1):
    print("\nJaneiro")

if(mes == 2):
    print("\nFevereiro")

if(mes == 3):
    print("\nMarço")
  
if(mes == 4):
    print("\nAbril")

if(mes == 5):
    print("\nMaio")

if(mes == 6):
    print("\nJunho")

if(mes == 7):
    print("\nJulho")

if(mes == 8):
    print("\nAgosto")

if(mes == 9):
    print("\nSetembro")
    
if(mes == 10):
    print("\nOutubro")

if(mes == 11):
    print("\nNovembro")

if(mes == 12):
    print("\nDezembro")

t = strftime("%X") 
hora = time.strftime("%H")
minu = time.strftime("%M")

print("\nHora Atual: {0}:{1}".format(hora,minu))


