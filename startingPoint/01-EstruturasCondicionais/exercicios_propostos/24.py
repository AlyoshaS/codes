"""24 - Faça um programa que receba a medida de um ângulo em graus. Calcule e mostre o quadrante em que se localiza esse 
ângulo. Considere os quadrantes da trigonometria e, para ângulos maiores que 360° ou menores que -360°, reduzi-los, 
mostrando também o número de voltas e o sentido da volta(horário ou anti-horário).
"""
angulo = int(input("Digite a medida do ângulo em graus: "))

if angulo > 360 or angulo < 360:
	voltas = angulo / 360
	angulo = angulo % 360
else:
	voltas = 0
if(angulo == 0) or (angulo == 90) or (angulo == 180) or (angulo == 270) or (angulo == 360) or (angulo == -90) or (angulo == -180) or (angulo == -270) or (angulo == -360):
	print("Está em cima de algum dos eixos.")
if (angulo > 0 and angulo < 90) or (angulo < -270 and angulo > -360):
	print("1° quadrante.")
if (angulo > 90 and angulo < 180) or (angulo < -180 and angulo > -270):
	print("2° quadrante.")
if (angulo > 180 and angulo < 270) or (angulo < -90 and angulo > -180):
	print("3° quadrante.")
if (angulo > 270 and angulo < 360) or (angulo < 0 and angulo > -90):
	print("4° quadrante.")

if (angulo < 0):
	print("No sentido: horário.")
else:
	print("No sentido: anti-horário.")
print("Número de voltas: ", voltas)
