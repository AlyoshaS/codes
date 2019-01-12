"""16 - Faça um programa para resolver equações do 2° grau.
ax² + bx + c = 0
A variável a deve ser diferente de zero.
∆ = b² - 4 * a * c
∆ < 0 -> não existe raiz real
∆ = 0 -> existe uma raiz real
x = (-b) / (2 * a)
∆ > 0 -> existem duas raízes reais
x1 = (-b + raizq(∆) / (2 * a))
x2 = (-b - raizq(∆) / (2 * a))
"""

# DEFINE a, b E c
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# DEFINE O VALOR DE DELTA, X1 E X2

if(a == 0):
    print("Estes valores não formam uma equação do segundo grau")
else:
    delta = (b ** 2) - (4 * a * c)
    if(delta < 0):
        print("Não existe raiz real")
        
    if(delta == 0):
        print("Existe uma raiz real")
        x1 = (-b) / (2 * a)
        print(x1)
        
    if(delta > 0):
        print("Existe duas raízes reais")
        raiz_delta = delta ** 0.5
        x1 = (-b + raiz_delta) / (2 * a)
        x2 = (-b - raiz_delta) / (2 * a)
        print("O valor de x1 é {0} e de x2 é {1}".format(x1, x2))
