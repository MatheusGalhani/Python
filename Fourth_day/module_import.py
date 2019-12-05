__author__ = "Matheus Galhani"

import datetime
import math
import random

if __name__ == '__main__':
    # Transforma uma data em uma string com determinada mascara
    day_string = datetime.datetime.now().strftime('%d/%m/%Y')
    print(f'Hoje é dia {day_string}')
    print(type(day_string))
    # Transforma uma string em datetime
    day = datetime.datetime.strptime(day_string, '%d/%m/%Y')
    print(f'Hoje é dia {day}')
    print(math.sqrt(4))
    print(random.randint(1, 10))
