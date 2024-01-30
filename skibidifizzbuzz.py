import numpy as np

def skibidifizzbuss(n):
    string = ""
    if n % 2 == 0:
        string += "skibidi"
    if n % 3 == 0:
        string += "fizz"
    if n % 5 == 0:
        string += "buzz"
    return string

def sibidifizzbuzz_vectorise(n):
    numbers = range(n)
    for i in range(n):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            numbers[i] = ""
        if i % 2 == 0:
            numbers[i] += "skibidi"
        if n % 3 == 0:
            string += "fizz"
        if n % 5 == 0:
            string += "buzz"
    return numbers
    


def cups_to_ml(ml):
    return 236.588 * ml

def ml_to_grams(ml, rho = 1):
    return ml * rho

def cups_to_ml(num_cups, ingedient = "water"):
    density = {"water" : 1, "flour" : 0.53, "oil" : 0.92, "oat_milk" : 1.03}
    vol = cups_to_ml(num_cups,)
    return ml_to_grams(vol, density[ingedient])


def Fibonacci(n):
    numbers = np.array([])
    numbers.append(1)
    numbers.append(1)
    for i in range(n-2):
        numbers[n+2].append(numbers[i]+numbers[i+1])
    return numbers

def my_cusum(array):
    cusum = 0
    for i in array:
        cusum += i
    return cusum


import pandas as pd
df = pd.read_excel("Tempexcel.xlsx")
df.to_latex("output.tex")

