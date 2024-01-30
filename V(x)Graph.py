from matplotlib import pyplot as plt
import numpy as np

#Parameters
d = 1
L = 1
V_0 = -1

#Performance
samples = 3000
bound = L


def f(x):
    if x < -L/2:
        return 0
    if (x >= -L/2) and (x <= L/2):
        return V_0
    if x > L/2:
        return 0

def psi1(x):
    if x < -L/2:
        return 1.649 * np.sin( x * np.pi * 6.95 )
    if (x >= -L/2) and (x <= L/2):
        return np.exp(-x)
    if x > L/2:
        return 0.6 * np.sin( (7*x-1) * np.pi )
    return 0

def psi2(x):
    if x < -L/2:
        return np.exp(x)
    if x > L/2:
        return np.exp( - x)
    if (x >= -L/2) and (x <= L/2):
        return 0.6095 * np.cos(np.pi * x * 4.06)
        
        

def sketch(f):
    x = [None] * samples
    y = [None] * samples
    for i in range(samples):
        x[i] = -bound + 2*i* bound/samples
        y[i] = f(x[i])

    plt.plot(x,y)
    plt.ylabel("Psi(x)")
    plt.xlabel("x Position")
    plt.title("Psi for V_0 < 0")
    plt.xticks([-L, -L/2, 0, L/2, L ], ["-L", "-L/2", "0", "L/2", "L"])
    plt.yticks([0], ["0"])
    plt.show()
    
