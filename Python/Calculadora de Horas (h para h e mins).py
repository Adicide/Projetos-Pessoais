# Calculadora de Horas (h --> h e min)

import math

tempo_h = float(input('Digite o tempo em horas (ex: 4.5)": '))
horas = int(tempo_h)
minutos = int((tempo_h-horas) * 60)

print(f'\n{tempo_h} h correspondem a {horas} h e {minutos} min.')