# Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
# O volume de um cilindro circular é calculado por meio da seguinte fórmula:
# V = π * raio² * altura, onde π = 3.141592.

altura = int(input("Digite a altura aqui: "))
raio = int(input("Digite o raio aqui: "))

PI = 3.141592
raio_a = raio ** 2
volume = (PI * raio_a * altura)

print("O volume do cilindro é: ", volume)

