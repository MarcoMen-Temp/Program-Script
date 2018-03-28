from math import sqrt
import functools
""" Start with 2520(range 1-10 -Given); 
    For range(11,21) print prime numbers =[11,13,17,19]
    Multiply all elements of the list between themselves and by 2520
    Test the result,by dividing it by all elements from 20 to 1
    It will fail at 16,compare the factorisation of 16 and the new result(2520x19x17) using count()2
    Append the 2 to the list and mutiply by 2
    Run the test again"""
# Stack OverFlow: 'Python Finding Prime Factors'

def prime_factors(x):
    x=2520
    '''x=232792560  # lcm of the first 10 natural numbers'''
    A=[]
    for i in range (2, x):
        while x%i==0:
            x=x/i

            A.append(i)

    if sum(A)==0:

        A.append(x)

    return A


print(prime_factors(2520)) # Able to print the factorisation of 2520-from line 5 Try to count the number of occurences for 2 in 2520 and 16"""


Primes = []
for n in range(11, 21):
    for x in range(2,n):
        if n % x ==0:
           
           break
    
    else:
        Primes.append(n)
        
        
print(Primes)  #Have to remove 2,3,4; and then multiply all remaining elements of list
               # And then test divisibility for range (20,2,-1) with return True or False 
                #How to multiply all items within a list?
product = 1
for x in Primes:
    product = product * x

print(product)
print (product * 2520)
