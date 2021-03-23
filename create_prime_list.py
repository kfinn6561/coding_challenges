'''
Created on 4 Mar 2020

@author: kieran
'''
import numpy as np
from general_tools import pdump,progress_bar
primes=[]

def check_prime(x):# assumes primes is an ordered list of all prime numbers
    if x in [0,1]:
        return False
    i=0
    stop=np.sqrt(x)
    while i<len(primes) and primes[i]<=stop:
        if x%primes[i]==0:
            return False
        i+=1
    return True


i=0
print np.sqrt(10**11)
while i<np.sqrt(10**11):
    if i%1000==0:
        print i
    if check_prime(i):
        primes.append(i)
    i+=1
        
pdump(primes,'prime_list.pkl')
        