""" 00 - A nota final de um estudante é calculada a partir de três notas atribuídas, respectivamente, 
a um trabalho de laboratório, a uma avaliação semestral e a um exame final.  Média das três notas mencionadas obedece 
aos pesos a seguir:

|NOTA   |PESO   |
|---|:-:|
| Trabalho de laboratório  | 2  |
| Avaliacao semestral  | 3  |
| Exame final  | 5  |

Faça um programa que receba as três notas, calcule e mostre a média e o conceito que segue a tabela:

|MÉDIA PONDERADA   |CONCEITO   |
|---|:-:|
| 8,0 **+**-----------**+** 10,0 | A  |
| 7,0 **+**----------**\*** 8,0  | B  |
| 6,0 **+**-----------**\*** 7,0  | C  |
| 5,0 **+**-----------**\*** 6,0  | D  |
| 0,0 **+**-----------**\*** 5,0  | E  |
"""
nota_trabalho = int(input("Digite a nota do Trabalho de Laboratório: "))
nota_avaliacao = int(input("Digite a nota da Avaliação Semestral: "))
nota_exame = int(input("Digite a nota do Exame Final: "))

# Define o peso das notas:
peso_trabalho = 2
peso_avaliacao = 3
peso_exame = 5

# Define a media das notas:
media = (nota_trabalho * peso_trabalho + nota_avaliacao * peso_avaliacao + nota_exame * peso_exame) / 10

# Define media emponderada:
if media >= 8 and media <= 10:
	print ("Obteve conceito A.")
if media >= 7 and media < 8:
	print("Obteve conceito B.")
if media >= 6 and media < 7:
	print("Obteve conceito C.")
if media >= 5 and media < 6:
	print("Obteve conceito D.")
if media >= 0 and media < 5:
	print("Obteve conceito E.")

