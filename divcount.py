'''
Created on 24 Feb 2021

@author: kieran
'''
'''returns the number of integers in the range A B that are divisible by K'''

import math

def solution(A, B, K):
    # write your code in Python 3.6
    div=math.floor((B-A+1)/K)
    remainder=(B-A+1)%K
    if (A-1)%K+remainder>=K:
        return div+1
    else:
        return div
    
def brute_force(A,B,K):
    out=0
    i=A
    while i<=B:
        if i%K==0:
            out+=1
        i+=1
    return out



def test(A,B,K):
    print('testing A=%d, B=%d, K=%d' %(A,B,K))
    fast=solution(A,B,K)
    slow=brute_force(A,B,K)
    if fast==slow:
        print('success!')
    else:
        print('fail!')
        
        
tests=[[6,11,2],
       [1,2,3],
       [5,5,5],
       [2,7,8],
       [55,76,5],
       [27,81,3]]

for t in tests:
    A,B,K=t
    test(A,B,K)