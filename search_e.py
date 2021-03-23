'''
Created on 4 Mar 2020

@author: kieran
'''
'''find the first 10 digit prime in consecutive digits of e'''


import numpy as np
from fractions import Fraction
from general_tools import pload

primes=pload('prime_list.pkl')

def digits_to_num(x_digits):
    out=0
    for i in range(len(x_digits)):
        out+=x_digits[-1-i]*(10**i)
    return out

def check_prime(x_digits):# assumes primes is an ordered list of all prime numbers
    x=digits_to_num(x_digits)
    if x in [0,1]:
        return False
    i=0
    stop=np.sqrt(x)
    while i<len(primes) and primes[i]<=stop:
        if x%primes[i]==0:
            return False
        i+=1
    return True

def factorial(x):
    out=1.
    while x>0:
        out*=x
        x-=1
    return out


class e_gen():
    def __init__(self):
        self.sf=0
        self.term=0
        self.value=Fraction()
        self.next_term=1
        self.add_term()
        
    def add_term(self):
        self.value+=Fraction(10**self.sf,self.next_term)
        self.term+=1
        self.next_term*=self.term
        self.next_sf=np.log10(float(self.next_term))-2#buffer
                
    def next_digit(self):
        while self.sf+1>=self.next_sf:
            self.add_term()
        out=int(self.value)
        if out>10:
            print out #debug
        self.value-=out
        self.value*=10
        self.sf+=1
        return out
       
       
e=e_gen()

digits=[]

for i in range(10):
    digits.append(e.next_digit())
    
counter=0
while counter<1000 and not check_prime(digits):
    print counter
    for i in range(1,len(digits)):
        digits[i-1]=digits[i]
    digits[-1]=e.next_digit()
    counter+=1
        
if counter<1000:
    print digits_to_num(digits)
        