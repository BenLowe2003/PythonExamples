from math import sqrt
from math import log
from copy import deepcopy

#Performance parameters
error_samples = 10
integral_samples = 50
integral_bound = 100
integral_resolution = integral_bound/integral_samples
decent_iterations = 1000
delta_init = 0.1
denemonator_terms = 4

#Constants
E0 = 1
tau = 1
mass = 1


#Initial Values
A_init = [1 for i in range(denemonator_terms)]



def error_function(A):
    error = 0
    for i in range(1, error_samples):
        E = E0 + 1/i
        integral = 0
        for i in range(1,integral_samples):
            x = i*integral_resolution
            U = 0
            for i in range(1,1+len(A)):
                U += A[i-1] * x**(-2*i)
            y =  ( 1 / ( sqrt( (E - U) ) ) - 1/sqrt(E) ) * integral_resolution
            integral += y
        integral = integral * 2
        err = ( - tau * log(E-E0) )/( sqrt(mass/2*E) * integral)
        error += (err-1)**2
    return error

def gen_U():
    A = A_init
    delta_A = [delta_init for i in range(len(A_init))]
    for i in range(decent_iterations):
        for i in range(len(A)):
            Ap = deepcopy(A)
            Am = deepcopy(A)
            Ap[i] = Ap[i] + delta_A[i]
            Am[i] = Am[i] - delta_A[i]

            err = error_function(A)
            errp = error_function(Ap)
            errm = error_function(Am)

            if (err <= errp) and (err <= errm):
                delta_A[i] = delta_A[i]/2
            elif (errp < err) :
                A = Ap
            elif (errm < err) :
                A = Am
    return A

print("Finding U(x), given specified parameters.")
A = gen_U()
print("U has been found.")


def U(xvalue):
    B = gen_U()
    sum_denominator = 0
    for i in range(1,1+len(B)):
        sum_denominator += B[i-1] * xvalue**(-2*i)
    U = sum_denominator
    
    return U
        





















        
                  

                
    
