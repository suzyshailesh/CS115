'''
Created on 10/11/18
@author:   Susmitha Shailesh
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return (n%2 != 0)

#101010

#For an odd base-10 number, the least-significant bit will be a 1 because
#2**0 = 1 is necessary to make a number odd. For an even base-10 number, the
#least-significant bit will be 0 because the number can be divided by 2 with
#no remainder.

#By eliminating the least-significant bit, the value of the original number
#is divided by 2 using integer division. For example, 1011 in binary is 11
#in decimal. 101 in binary is 5 in decimal, which is 11//2.

#If N is odd, you would add a 1 to the end of N to get Y.
#If N is even, you would add a 0 to the end of N to get Y.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2) + "1"
    else: return numToBinary(n//2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binToNum(s, n, acc):
        '''helper function using tail recursion'''
        if s == "":
            return acc
        else:
            return binToNum(s[:-1], n+1, acc + (int(s[-1]))*(2**n))
    return binToNum(s, 0, 0)


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == "11111111":
        return "00000000"
    else:
        answer = numToBinary(binaryToNum(s)+1)
        if len(answer) == 8:
            return answer
        elif len(answer) > 8:
            return "00000000"
        else:
            def addZeros(n, l):
                '''makes n a string with 8 bits by adding 0's to the beginning'''
                if l == 8:
                    return n
                else: return addZeros("0" + n, l+1)
        return addZeros(answer, len(answer))
    

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return
    else: count(increment(s), n-1)

#The ternary representation for 59 is 2012. This is because
# 59 = 2*1 + 1*3 + 0*9 + 2*27.

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n%3 == 1:
        return numToTernary(n//3) + "1"
    elif n%3 == 2:
        return numToTernary(n//3) + "2"
    else: return numToTernary(n//3) + "0"

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def ternToNum(s, n, acc):
        if s == "":
            return acc
        else:
            return ternToNum(s[:-1], n+1, acc + (int(s[-1]))*(3**n))
    return ternToNum(s, 0, 0)
