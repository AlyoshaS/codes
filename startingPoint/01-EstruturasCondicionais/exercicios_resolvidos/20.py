"""
20 - Faça um programa que receba o preço de um produto e seu código de origem e mostre sua procedência. A procedência obedece à tabela a seguir.

| CÓDIGO DE ORIGEM           | PROCEDÊNCIA     |
|----------------------------|-----------------|
| 1                          | Sul             |
| 2                          | Norte           |
| 3                          | Leste           |
| 4                          | Oeste           |
| 5 ou 6                     | Nordeste         |
| 7 ou 8 ou 9                | Sudeste         |
| 10 a 20                    | Centro-oeste    |
| 21 a 30                    | Nordeste        |
"""
preco = float(input("Digite o preço do produto: "))
codigo_origem = int(input("Digite o código de origem: "))

if codigo_origem == 1:
	print("Procedência: Sul.")
elif codigo_origem == 2:
	print("Procedência: Norte.")
elif codigo_origem == 3:
	print("Procedência: Leste.")
elif codigo_origem == 4:
	print("Procedência: Oeste.")
elif codigo_origem <= 6:
	print("Procedência: Nordeste.")
elif codigo_origem <=9:
	print("Procedência: Sudeste.")
elif codigo_origem <= 20:
	print("Procedência: Centro-oeste.")
elif codigo_origem <= 30:
	print("Procedência: Nordeste.")
else:
        print("Código de origem inválido!")
