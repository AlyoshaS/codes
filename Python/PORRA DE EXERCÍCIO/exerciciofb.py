"""
Faça um programa para uma loja de tintas:
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertuta da tinta é de 1 litro para cada 6 metros quadrados e que a tinda é vendida em:
latas de 18 litros, que custam R$ 80,00 ou em galões da 4 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        comprar apenas latas de 18 litros;
        comprar apenas galões de 4 litros;
        misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias!
Dica: Você usará Int(), //, % e if.
"""
# Recebe os dados do usuario:
metros_quadrados = int(input("Digite a área a ser pintada em metros quadrados(m²): "))

# Define a folga de tinta, quantidade de litros por área, de latas, galões e o preco da lata e do galao:
litros = metros_quadrados / 6
folga = .10
total_litros = int(litros + (litros * folga))
preco_lata = 80.00
preco_galao = 25.00

# Define total de litros a ser utilizado:
if total_litros %6 > 0:
	litros_total = litros + 1
	total_litros = int(litros + (litros * folga))
	print("A quantidade de litros a ser utilizada: ", total_litros)
	
# Define a quantidade de tinta a comprar apenas em latas e seu respectivo valor:
latas = total_litros // 18
if total_litros %18 > 0:
        quantidade_de_latas = latas + 1
        preco_total_latas = round(quantidade_de_latas * preco_lata, 2)
        print("Você precisará de ", quantidade_de_latas, "latas de 18 litros e o valor será de R$", preco_total_latas)

# Define a quantidade de tinta a comprar apenas em galoes e seu respectivo valor:
galoes = total_litros // 4
if total_litros %4 > 0:
        quantidade_de_galoes = galoes + 1
        preco_total_galoes = round(quantidade_de_galoes * preco_galao, 2)
        print("Você precisará de ", quantidade_de_galoes, "galões de 4 litros e o valor será de R$", preco_total_galoes)

# Define a quantidade de tinta a comprar em galoes e latas e seus respectivos valores:
if total_litros %18 > 0:
        if
        total_latas = latas
        total_litros % 18 
        print(total_galoes)
