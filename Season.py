from enum import Enum


class Season(Enum):
    WINTER = 1
    SUMMER = 2
    SPRING = 3
    FALL = 4

temporada = Season.SUMMER.name
if temporada is Season.SUMMER.name:
    print('Verano')
elif temporada is Season.WINTER.name:
    print('Invierno')
elif temporada is Season.FALL.name:
    print('Otoño')
elif temporada is Season.SPRING.name:
    print('Primavera')

lista = list(Season)
for s in lista:
    print(f'{s.name}')
