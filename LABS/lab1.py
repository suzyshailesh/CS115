
#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *
from math import *
import math

def inverse(n):
    '''returns the inverse of input n'''
    return (1/n)

def e(n):
    '''returns an approximation of e as a Taylor polynomial with n+1 terms'''
    L = range(1,n+1)
    L2 = map(factorial,L)
    L3 = map(inverse,L2)
    return(1+sum(L3))

def error(n):
    '''returns the absolute value of the difference between e and the Taylor
    approximation for e with n+1 terms'''
    taylor = e(n)
    actual = math.e
    answer = abs(taylor-actual)
    return answer

