""" 04 - Faça um progama que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do 
usuário.

| ESCOLHA DO USUÁRIO            | OPERAÇÃO                             |
|-------------------------------|--------------------------------------|
| 1                             | Média entre os números digitados     |
| 2                             | Diferença do maior pelo menor        |
| 3                             | Produtos entre os números digitados  |
| 4                             | Divisão do primeiro pelo segundo     |

Se a opção digitada for inválida, mostre uma mensagem de erro e termine a execução do programa. 
Lembre-se que, na operação 4, o segundo número deve ser diferente de zero.
"""
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo número: "))
print("\n")
print("+---------------------+--------------------------------------+")
print("|      Opções:        |             Operação:                |")
print("|---------------------|--------------------------------------|")
print("|         1           | Média entre os números digitados     |")
print("|         2           | Diferença do maior pelo menor        |")
print("|         3           | Produtos entre os números digitados  |")
print("|         4           | Divisão do primeiro pelo segundo     |")
print("+---------------------+--------------------------------------+")
print("\n")
operacao = int(input("Digite a operação desejada de acordo com a lista acima: "))
 
if operacao == 1:
	print("A média entre os números {0} e {1} é igual a {2}!".format(numero1, numero2, ((numero1 + numero2) / 2)))

if operacao == 2:
	if numero1 > numero2:
		print("A diferença entre os números {0} e {1} é igual a {2}!".format(numero1, numero2, (numero1 - numero2)))
	elif numero2 > numero1:
		print("A diferença entre os números {0} e {1} é igual a {2}!".format(numero2, numero1, (numero2 - numero1)))
	else:
		print("Os números são iguais! A diferença é igual a 0!")

if operacao == 3:
	print("O produto entre os números {0} e {1} é igual a {2}!".format(numero1, numero2, (numero1 * numero2)))

if operacao == 4:
	print("A divisão entre os números {0} e {1} é igual a {2}!".format(numero1, numero2, (numero1 / numero2)) if numero2 != 0 else "O segundo número deverá ser diferente de 0!" )

else:
	print("Operação inválida!")