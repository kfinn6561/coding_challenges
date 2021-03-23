'''
Created on 24 Feb 2021

@author: kieran
'''
'''Input is an array of length N, representing the number of filled cells in each column of an NxN grid (all columns fill up from the bottom.
Determines the side of the largest possible filled square'''


import math
from numpy.random import randint

def visualise(A):
    N=len(A)
    for i in range(N):
        out=''
        for a in A:
            if a>=N-i:
                out+='#'
            else:
                out+=' '
        print(out)


def brute_force(A):
    # write your code in Python 3.6
    out=len(A)
    while out>1:
        count=0
        for a in A:
            if a>=out:
                count+=1
                if count>=out:
                    return out
            else:
                count=0
        out-=1
    return out

def find_min(A):
    if len(A)==0:
        return((0,0))
    mn=A[0]
    out=0
    for i in range(1,len(A)):
        if A[i]<mn:
            mn=A[i]
            out=i
    return (out,mn)
    
    


def solution(A):
    i,mn=find_min(A)
    #print('\n')
    #visualise(A)
    #print(len(A),mn)
    if len(A)<=mn:
        return len(A)
    else:
        return max(mn,solution(A[:i]),solution(A[i+1:]))


def test(A):
    visualise(A)
    if brute_force(A)==solution(A):
        print('success')
        return 1
    else:
        print('fail')
        return 0
 
 
As=[]     
N_tests=50
score=0
for i in range(N_tests):
    N=randint(2,21)
    print('\n\n')
    print('Test %d' %i)
    A=randint(1,N,N)
    As.append(A)
    score+=test(A)
    
print('Result: %d out of %d' %(score, N_tests))