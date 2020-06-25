#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *

def dot(L,K):
    '''returns the dot product of L and K'''
    if L == []: 
        if K == []:
            return 0.0
        else: return 0.0
    elif K == []:
        return 0.0
    else: return ((L[0]*K[0]) + dot(L[1:], K[1:]))
    
def explode(S):
    '''returns a list of characters in string S'''
    if S == "":
        return []
    else: return [S[0]] + explode(S[1:])

def ind(e,L):
    '''returns the first index of L at which e is found'''
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1+ind(e,L[1:])

def removeAll(e,L):
    '''returns a list with all the elements in L except for e'''
    if L == []:
        return []
    elif L[0] == e:
        return ([] + removeAll(e,L[1:]))
    else: return [L[0]] + removeAll(e,L[1:])

def even(x):
    '''returns True if x is even and False if x is odd'''
    if x%2 == 0: return True
    else: return False

def myFilter(f,L):
    '''returns list with all elements of list L that return True for function f'''
    if L == []:
        return []
    elif f(L[0]) == True:
        return ([L[0]] + myFilter(f,L[1:]))
    else: return myFilter(f,L[1:])

def deepReverse(L):
    '''returns the reverse of list L'''
    if L == []:
        return []
    elif isinstance(L[0],list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]







    
