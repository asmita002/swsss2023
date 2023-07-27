#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Asmita Pramanik'
__email__ = 'asmitap2@illinois.edu'

from math import factorial
from math import pi


def cos_approx(x, accuracy=20):
    """This function finds the cosine approximation using Taylor series
    Args:
        x(float):
            to evaluate cosine of.
        accuracy (int):
    (default: 10) Number of Taylor series coefficents"""
    sum = 0  #cos_approx
    
    for n in range(accuracy+1): #range depends on the accuracy value
        sum = sum + (((-1)**n / (factorial(2*n))) * (x**(2*n)))
        
    return sum



# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
