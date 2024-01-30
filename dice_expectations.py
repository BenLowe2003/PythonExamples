import random as rand
import matplotlib.pyplot as plt
import math as math

def expected_num_rolls(max_dice, num_tests):
    sum_num_rolls = 0
    for i in range(num_tests):
        achieved = False
        num_dice = 1
        num_rolls = 0
        while achieved == False:
            rolls = [ rand.randint(1,6) for i in range(num_dice) ]
            num_rolls += 1
            is_success = True
            for i in range(len(rolls)):
                if rolls[i] <=2 :
                    is_success = False
            if is_success:
                num_dice += 1
            if num_dice >= max_dice:
                sum_num_rolls += num_rolls
                achieved = True
    expectation = sum_num_rolls/num_tests
    return expectation

def plot_expected_rolls(num_tests, max_dice):
    expectations = [0]*max_dice
    for i in range(max_dice):
        expectations[i] = expected_num_rolls(i+1,num_tests)
    x = [ i+1 for i in range(max_dice)]
    plt.plot(x ,expectations)

    y = [ 1.5**(a)for a in x]

    plt.plot(x,y)
    
    plt.show()
