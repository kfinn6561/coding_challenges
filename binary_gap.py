'''
Created on 24 Feb 2021

@author: kieran
'''

'''finds the largest gap of 0s, surrounded by 1s in the binary representation of a number'''

def solution(N):
    bin_string=bin(N)[2:]#ignore the '0b' string
    out=0
    i=0
    while True:
        while bin_string[i]=='1':
            i+=1
            if i>=len(bin_string):
                return out
        temp=0
        while bin_string[i]=='0':
            i+=1
            if i>=len(bin_string):
                return out
            temp+=1
        if temp>out:
            out=temp