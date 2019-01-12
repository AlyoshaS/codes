"""10 - Faça um programa que receba a hora do início de um jogo e a hora final (cada hora é composta por duas variáveis 
inteiras: hora e minuto). Calcule e mostre a duração do jogo(horas e minutos), sabendo-se que o tempo máximo de duração do 
jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte.
"""
print("Digite o horário inicial: ")
hora_i = int(input("Hora: "))
min_i = int(input("Minuto: "))

print("Digite o horário final: ")
hora_f = int(input("Hora: "))
min_f = int(input("Minuto: "))

if(min_i > min_f):
    min_f = min_f + 60
    hora_f = hora_f - 1

if(hora_i > hora_f):
    hora_f = hora_f + 24

min_d = min_f - min_i
hora_d = hora_f - hora_i

print("O jogo durou ",hora_d," hora(s) e ",min_d," minutos(s)")


            
