from math import sqrt


def primes(n):
    return [ i for i in range(2,n) if i not in [ p*q for p,q in range(2,n)] ]
