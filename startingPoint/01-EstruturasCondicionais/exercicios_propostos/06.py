""" 6 - Faça um programa que receba quatro valores I, A, B, C. Desses valores, I é inteiro e positivo, A, B e C são reais. 
Escreva os números A, B e C obedecendo à tabela a seguir.

Suponha que o valor digitado para I seja sempre um valor válido, ou seja, 1, 2 ou 3, e que os números digitados sejam
diferentes um do outro.

VALOR DE I	FORMA DE ESCREVER
1	A, B, C em ordem crescente
2	A, B, C em ordem decrescente
2	O maior fica entre os outros dois números
"""
A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))
C = int(input("Digite um valor para C: "))
I = int(input("Digite um valor para I (1, 2, ou 3): "))

#1 A, B, C em ordem crescente

if(I == 1):
        if(A < B) and (A < C):
                if(B < C):
                        print("A ordem crescente é {0} - {1} - {2}.".format(A, B, C))

                else:
                        print("A ordem crescente é {0} - {1} - {2}.".format(A, C, B))

        if(B < A) and (B < C):
                if(A < C):
                        print("A ordem crescente é {0} - {1} - {2}.".format(B, A, C))
                else:
                        print("A ordem crescente é {0} - {1} - {2}.".format(B, C, A))

        if(C < A) and (C < B):
                if(A < B):
                        print("A ordem crescente é {0} - {1} - {2}.".format(C, A, B))
                else:
                        print("A ordem crescente é {0} - {1} - {2}.".format(C, B, A))                    
	
#2 A, B, C em ordem decrescente

if(I == 2):
        if(A > B) and (A > C):
                if(B > C):
                        print("A ordem decrescente é {0} - {1} - {2}.".format(A, B, C))
                else:
                        print("A ordem decrescente é {0} - {1} - {2}.".format(A, C, B))

        if(B > A) and (B > C):
                if(A > C):
                        print("A ordem decrescente é {0} - {1} - {2}.".format(B, A, C))
                else:
                        print("A ordem decrescente é {0} - {1} - {2}.".format(B, C, A))
	
        if(C > A) and (C > B):
                if(A > B):
                        print("A ordem decrescente é {0} - {1} - {2}.".format(C, A, B))
                else:
                        print("A ordem decrescente é {0} - {1} - {2}.".format(C, B, A))

#3 O maior fica entre os outros dois números

if(I == 3):
	if(A > B) and (A > C):
		print("A ordem desejada é {0} - {1} - {2}.".format(B, A, C))
	if(B > A) and (B > C):
		print("A ordem desejada é {0} - {1} - {2}.".format(A, B, C))
	if(C > A) and (C > B):
		print("A ordem desejada é {0} - {1} - {2}.".format(A, C, B))

