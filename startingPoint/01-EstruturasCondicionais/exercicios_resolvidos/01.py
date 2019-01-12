"""01 - Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que se encontra
na tabela a seguir:

| MÉDIA ARITMÉTICA              | MENSAGEM                   |
|-------------------------------|----------------------------|
| 0,0 *----° 4,0                | Reprovado                  |
| 4,0 *----° 7,0                | Exame                      |
| 7,0 *----* 10,0               | Aprovado                   |
"""
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("Média aritmética: ", media)

if media >= 0 and media < 4:
	print("Reprovado.")
if media >= 4 and media < 7:
	print("Exame.")
if media >= 7 and media <= 10:
	print("Aprovado!")
