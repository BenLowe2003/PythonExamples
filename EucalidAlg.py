
import numpy as np

A = float(input("A = "))    #input arguments
B = float(input("B = "))
r = float(1)                #define the remainder

if A > B :                  #Determine which of the arguments will be a and b in the algorithem
    a = A
    b = B
elif B > A :
    a = B
    b = A
elif A ==B:
    exit()





while r != 0 :                          # while loop for the remainder being none zero
    Q = np.floor(a/b)                 # Finds quotient
    r = a - ( Q * b)                    # Finds remainder

    print(a, "=", Q, "*", b, "+", r)    # Print each line of working



    
    
    a = b                               #Interate on a and b.
    b = r

print( "HCF(" + str(A) + ", " + str(B) + ") = " + str(a) )
    
