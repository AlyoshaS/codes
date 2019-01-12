""" 09 - Faça um programa que determine a data cronologicamente maior entre duas datas fornecidas pelo usuário. Cada data deve 
ser composta por três valores inteiros, em que o primeiro representa o dia, o segundo, o mês e o terceiro, o ano.
"""

print("Digite a primeira data: ")
d1 = int(input("Dia (dd): "))
m1 = int(input("Mes (mm): "))
a1 = int(input("Ano (aaaa): "))

print("Digite a segunda data: ")
d2 = int(input("Dia (dd): "))
m2 = int(input("Mes (mm): "))
a2 = int(input("Ano (aaaa): "))

if(a1 > a2):
    print("A maior data é: ",d1,"-",m1,"-",a1)

elif(a2 > a1):
    print("A maior data é: ", a2,"-",m2,"-",a2) 

elif(m1 > m2):
    print("A maior data é: ",d1,"-",m1,"-",a1)

elif(m2 > m1):
    print("A maior data é: ",d2,"-",m2,"-",a2)

elif(d1 > d2):
    print("A maior data é: ",d1,"-",m1,"-",a1)

elif(d2 > d1):
    print("A maior data é: ",d2,"-",m2,"-",a2)

else:
    print("As datas são iguais!")

            
