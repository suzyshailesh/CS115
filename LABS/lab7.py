#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

# lab exercise: circuits in Python 

# Study the comments and code provided,
# before doing the exercises.


# Logical gates; should only be applied
# to "bits", i.e., either 0 and 1
def gnot(x):
    '''returns not x'''
    assert x in [0,1]
    return int(not(x)) 
def gand(x,y):
    '''returns x and y'''
    assert x in [0,1] and y in [0,1]
    return x and y
def gor(x,y):
    '''returns x or y'''
    assert x in [0,1] and y in [0,1]
    return x or y


# Example: XOR
# Definition x y | x xor y
#            0 0 | 0
#            0 1 | 1
#            1 0 | 1
#            1 1 | 0
# Expression for the 1 rows, using ! for not
#   !xy + x!y 
# Code using only gates:
def XOR(x,y):
    '''checks if only 1 number is 1'''
    return gor( gand(gnot(x),y), gand(x,gnot(y)) )

def testXOR():
    '''tests XOR'''
    assert XOR(0,0) == 0
    assert XOR(0,1) == 1
    assert XOR(1,0) == 1
    assert XOR(1,1) == 0
    print("testXOR success")


# EXERCISE
# Define this function as a single return using
# only the logical gate functions.
def gor3(x,y,z):
    '''Or of three inputs.'''
    return gor(gor(x,y),z)


# EXERCISE
# Full adder.  See Lecture 6 slide 10
# Implement this as a single return, using only
# the logical gate functions, like XOR.
# You may also use gor3 or similar helper functions
# that you write. And you may use assigned-once variables:
# think of those as named wires.

def check1(x,y,z):
    '''checks to see if a single number is 1'''
    return XOR(XOR(x,y),z)

def check2(x,y,z):
    '''checks to see if two numbers are 1'''
    return XOR(XOR(gand(x,y),gand(y,z)),gand(x,z))

def gand3(x,y,z):
    '''tests to see if all numbers are 1'''
    return gand(gand(x,y),z)

def FA(x,y,cin):
    '''Assume x, y, and cin are bits.
    Return the pair of bits (carry_out,sum) such that
    sum is the low bit of x+y+cin and carry_out is
    the high bit of x+y+carry_in.'''
    s = check1(x,y,cin)
    cout = check2(x,y,cin)
    return (cout,s)

            
def FAtest(x,y,c):
    '''Compute FA using integer arithmetic.'''
    s = (x+y+c) % 2
    d = 1 if x+y+c >= 2 else 0
    return (d,s)

def testFA():
    '''tests FA'''
    assert FA(0,0,0) == FAtest(0,0,0) 
    assert FA(0,1,0) == FAtest(0,1,0) 
    assert FA(1,1,1) == FAtest(1,1,1)
    print("testFA successful on 3 out of 8 cases")


# Review slide 12 of Lecture 6 before continuing.

def twoBitAdd(xx,yy):
    '''Assume xx and yy are pairs (xt,xo) and (yt,yo) of bits.
    Return (cout,(zt,zo)) where (zt,zo) is their two-bit sum
    is the carry bit. Note: xo is the one's place and xt is
    the two's place.  ALERT: use the notation xx[0] to refer to xt,
    and xx[1] to refer to xo.'''
    (c,zo) = FA(xx[1],yy[1],0)
    (d,zt) = FA(xx[0],yy[0],c)
    return (d,(zt,zo))
# Notice the assignments to two variables at once,
# which only works if the right-hand side evaluates to a pair.


def test_twoBitAdd():
    '''tests twoBitAdd'''
    zero = (0,0)
    one = (0,1)
    two = (1,0)
    three = (1,1)
    c,ww = twoBitAdd(one,zero)
    assert( ww == (0,1) and c == 0 )
    c,ww = twoBitAdd(one,one)
    assert( ww == (1,0) and c == 0 )
    c,ww = twoBitAdd(three,three)
    assert( ww == (1,0) and c == 1 )
    print("test_twoBitAdd worked (but incomplete test)")


# EXERCISE: implement the following, using gates and/or FA.
# Hint: you might start by defining something like twoBitAdd
# but that also has a carry input.

def fourBitAdd(xxxx,yyyy):
    '''Assume xxxx is a quadruple (xe,xf,xt,xo) of four bits,
    with xe the high-order bit (i.e., eight's place).  Likewise
    yyyy.  Return (c,zzzz) where zzzz is their four-bit sum
    and c is the carry.'''
    (a,z4) = FA(xxxx[3],yyyy[3],0)
    (b,z3) = FA(xxxx[2],yyyy[2],a)
    (c,z2) = FA(xxxx[1],yyyy[1],b)
    (d,z1) = FA(xxxx[0],yyyy[0],c)
    return (d,(z1,z2,z3,z4))

# EXERCISE: implement the following.
def test_fourBitAdd():
    '''at least four test cases'''
    assert fourBitAdd((0,0,0,0), (0,0,0,0)) == (0, (0,0,0,0))
    assert fourBitAdd((0,0,0,1), (0,0,0,0)) == (0, (0,0,0,1))
    assert fourBitAdd((0,0,1,0), (0,0,0,0)) == (0, (0,0,1,0))
    assert fourBitAdd((0,0,1,1), (0,0,0,0)) == (0, (0,0,1,1))
    assert fourBitAdd((1,0,1,0), (1,0,1,0)) == (1, (0,1,0,0))
    assert fourBitAdd((1,1,1,0), (1,1,1,0)) == (1, (1,1,0,0))
    assert fourBitAdd((1,0,1,1), (0,1,0,1)) == (1, (0,0,0,0))
    assert fourBitAdd((0,0,1,0), (0,0,0,1)) == (0, (0,0,1,1))
    assert fourBitAdd((1,0,0,0), (1,0,0,0)) == (1, (0,0,0,0))
    assert fourBitAdd((1,1,1,1), (0,1,1,0)) == (1, (0,1,0,1))

    
