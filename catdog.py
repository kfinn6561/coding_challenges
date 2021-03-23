'''
Created on 9 Mar 2021

@author: kieran
'''

'''determines whether a group can swap pets so that everyone has their preference, given a limited number of connections'''

import math

def binsearch(A, X):
    N = len(A)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r + 1) // 2#ensures even length arrays are split in half
        if A[m] > X:
            r = m - 1
        else:
            l = m
    return A[l] == X

def merge_lists(A,B):
    NA=len(A)
    NB=len(B)
    A.append(math.inf)
    B.append(math.inf)
    out=[]
    i=0
    j=0
    while len(out)<NA+NB:
        if A[i]>B[j]:
            out.append(B[j])
            j+=1
        else:
            out.append(A[i])
            i+=1
    return(out)


def find_group(x,groups):
    for i in range(len(groups)):
        if binsearch(groups[i],x):
            return i
    return -1#shouldn't happen

def solution(P, T, A, B):
    # write your code in Python 3.6
    N=len(P)
    M=len(A)

    groups=[[i] for i in range(N)]
    for i in range(M):
        a=A[i]
        b=B[i]
        ga=find_group(a,groups)
        gb=find_group(b,groups)
        if ga!=gb:
            groups[ga]=merge_lists(groups[ga],groups[gb])
            del groups[gb]


    for group in groups:
        out=0
        for i in group:
            out+=P[i]-T[i]
        if out!=0:
            return False
    return True