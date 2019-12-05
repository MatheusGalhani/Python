__author__ = "Matheus Galhani"

from datetime import datetime
from math import sqrt
from random import *

if __name__ == '__main__':
    # Transforma uma data em uma string com determinada mascara
    day_string = datetime.now().strftime('%d/%m/%Y')
    print(f'Hoje é dia {day_string}')
    print(type(day_string))
    # Transforma uma string em datetime
    day = datetime.strptime(day_string, '%d/%m/%Y')
    print(f'Hoje é dia {day}')
    print(sqrt(4))
    print(randint(1, 10))
