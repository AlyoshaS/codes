"""
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor de E, conforme a fórmula a seguir:
E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

DECLARE n, e, i, j, fat NUMERICO

LEIA n
e <- 1

PARA i <- 1 ATÉ n FAÇA
    fat <- 1
    PARA j <- 1 ATÉ i FAÇA
        fat <- fat * j
    e <- e + 1/fat

ESCREVA e
"""
n = int(input("Digite o número(inteiro e positivo): "))
e = 1

for i in range(1, n+1):
	fat = 1
	for j in range(1, n+1):
                fat = fat * j
		e = e + 1/fat

print("E = %d" % e)
