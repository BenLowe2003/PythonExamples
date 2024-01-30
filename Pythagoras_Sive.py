import numpy as np
from math import floor, ceil

def prime_numbers_sive(uptoo):
    numbers = [i+2 for i in range(uptoo-2)]
    for i in range(floor(uptoo/2)):
        for j in range(ceil(uptoo/(i+1))):
            composite = (i+2)*(j+2)
            if composite in numbers:
                numbers.remove(composite)
    return numbers

    
    
