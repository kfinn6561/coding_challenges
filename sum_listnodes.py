'''
Created on 24 Feb 2021

@author: kieran
'''
'''adds two numbers given a list node of their digits'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def list_to_ln(A):
    out=None
    for i in range(len(A)-1,-1,-1):
        out=ListNode(A[i],out)
    return out
        
def ln_to_list(ln):
    out=[]
    while ln:
        out.append(ln.val)
        ln=ln.next
    return out
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    ls=[l1,l2]
    out=[]
    carry=0
    while ls[0] or ls[1]:
        dig=carry
        for i in range(2):
            if ls[i]:
                dig+=ls[i].val
                ls[i]=ls[i].next
        if dig>=10:
            carry=1
            dig=dig%10
        else:
            carry=0
        out.append(dig)
    if carry==1:
        out.append(1)
    LN_out=None
    
    for i in range(len(out)-1,-1,-1):
        LN_out=ListNode(out[i],LN_out)
    return LN_out


l1=list_to_ln([2,4,3])
l2=list_to_ln([5,6,4])

print(addTwoNumbers(l1,l2))