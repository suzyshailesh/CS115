
#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *

def mult(x,y):
    '''returns the product of x and y'''
    return x*y

def factorial(n):
    '''returns the factorial of n'''
    L = range(1,n+1)
    return reduce(mult,L)

def add(x,y):
    '''returns the sum of x and y'''
    return x+y

def mean(L):
    '''returns the average of list L'''
    num = reduce(add,L)
    den = len(L)
    return num/den

def divides(n):
    '''returns function div'''
    def div(k):
        '''checks if the remainder of n%k is 0'''
        return n%k == 0
    return div

def prime(n):
    '''returns true if n is prime and false if n is composite'''
    L = range(2,n)
    return sum(map(divides(n),L))== 0
    

    
