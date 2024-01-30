

#Initial values
function_parameters = [1,1,1]
delta_innit = 0.1


def test_function(A):
    total = 0
    x = 5
    for i in range(len(A)):
        total += A[i] * x ** i
    return total

def grad_decent(test_function, innitial_parameters, generations):
    num_parameters = len(innitial_parameters)
    A1 = innitial_parameters
    A2 = [None] * num_parameters
    error1 = [None] * num_parameters
    error2 = [None] * num_parameters
    delta_initial = 0.1

    for i in range(num_parameters):
        error1[i] = test_function(A)
        A2[i] = A1[i] +  delta_innit

        
    for i in range(generations):
        for i in range(num_parameters):
            error2[i] = test_function(A2)
            A_temp = ( error2[i] * ( A2[i] - A1[i] ) )/( error2[i] - error1[i] ) - A2[i]
            A2[i] = A_temp
        A1 = A2
    return A1

            

    
    for i in range(num_parameters):
        error2[i] = test_function(A)
        A_temp = ( error2[i] * ( A_new[i] - A[i] ) )/( error2[i] - error1[i] ) - A_new[i]

    A = A_new
    error1 = error2
