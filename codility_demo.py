'''
Created on 24 Feb 2021

@author: kieran
'''
'''returns smallest positive integer not present in the list'''

def solution(A):
    if 1 not in A:
        return 1
    A.sort()
    i=0
    while A[i]<1:
        i+=1
        
    while i+1<len(A) and A[i+1]-A[i]<=1:
        i+=1
    
    return A[i]+1
        
      
    
    


    