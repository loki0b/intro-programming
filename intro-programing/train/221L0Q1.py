from math import sqrt
from math import pow

X = int(input())
Z = int(input())

hogsmeade = sqrt(pow((X - 34), 2) + pow((Z - 220), 2))
kakariko = sqrt(pow((X - 0), 2) + pow((Z - 0), 2))
solitude = sqrt(pow((X - 140), 2) + pow((Z - 456), 2))

print(f'Distancia para Hogsmeade: {hogsmeade:.2f}')
print(f'Distancia para Kakariko: {kakariko:.2f}')
print(f'Distancia para Solitude: {solitude:.2f}')