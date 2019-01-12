# Entrada de dados:

segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

# Conversao para dias, horas, minutos e segundos:

dias = total_segs // 86400
segs_restantes = int(total_segs % 86400)

horas = segs_restantes // 3600
segs_restantes1 = int(total_segs % 3600)

minutos = int(segs_restantes1 // 60)
segs_rest_final = int(segs_restantes1 % 60)

# Saída de dados:

print(dias, "dias", horas, "horas, ", minutos, "minutos e", segs_rest_final, "segundos.")
