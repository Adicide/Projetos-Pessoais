# Calculadora de Horas (h e min --> h) 

import math

tempo_h = float(input('Digite as horas (ex: 1h): '))
tempo_m = float(input('Digite os minutos (ex: 30min): '))

horas = int(tempo_h)
minutos = float((tempo_m) / 60)
tempo_final = float(horas + minutos)

print(f'\n{horas} h e {tempo_m:.0f} min correspondem a {tempo_final:.2f} h.')