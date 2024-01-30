from matplotlib import pyplot as plt
import numpy as np

#parameters

L = 1
A = np.sqrt(2/L)
n = 1

samples = 100
resolution = L/samples


x = np.arange(0,L,resolution)
y = [0]*samples

def psi(x):
    y = A * np.sin((np.pi * n * x)/L)
    return y

for i in range(samples):
    y[i] = (psi(x[i]))**2

plt.plot(x,y)
plt.ylabel("Probability Density")
plt.xlabel("x Position")
plt.title("Probability Distribution For An Infinite Square Well, n = 1")
plt.xticks([0,1],["0","L"])
plt.yticks([0,2],["0","2 / L"])
plt.ylim(0, None)
plt.xlim(0,None)


plt.show()


