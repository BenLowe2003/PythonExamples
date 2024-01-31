idel// Prime_Num_Generator.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

int main()
{
    std::cout << "Hello World!\n";

    int prime_sive(int uptoo) {
        int numbers[uptoo];
        for (int i = 0 : i < uptoo : i++) {
            numbers[i] = i + 1;
        }

        // remove the composite numbers from the numbers array 
        int composite = 0;
        for (int i = 2; i < (uptoo / 2); i++) {
            for (int j = 2; j*i < uptoo; j++) {
                composite = i*j;
                bool in_numbers = false;
                for (int k = 0; k < uptoo; k++) {
                    if (numbers[k] == composite) {
                        in_numbers = true ;
                    }
                }
                if (in_numbers) { 
                    numbers[composite] = 0 ;
                }
            }
        }

        //count how many primes we've generated
        int num_primes = 0;
        for (int i = 0 : i < uptoo; i++) {
            if (numbers[i] > 0) {
                num_primes++;
            }
        }

        //write the primes in a new array
        int prime_index = 0;
        int primes[num_primes];
        for (int i = 0 : i < uptoo; i++) {
            if (numbers[i] > 0) {
                primes[prime_index] = numbers[i];
                prime_index++;
            }
        }

        return primes



    }

}







// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
