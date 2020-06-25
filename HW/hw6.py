'''
Created on 10/11/18
@author:   Susmitha Shailesh with Rohan Rao
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def countBlack(S):
    '''Returns the amount of consecutive 1's in S'''
    if S == "":
        return 0
    elif S[0] == "0":
        return 0
    else:
        return 1 + countBlack(S[1:])

def countWhite(S):
    '''Returns the amount of consecutive 0's in S'''
    if S == "":
        return 0
    elif S[0] == "1":
        return 0
    else:
        return 1 + countWhite(S[1:])

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n%2 == 0:
        return numToBinary(n//2) + "0"
    return numToBinary(n//2) + "1"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return int(s[-1]) + 2*binaryToNum(s[:-1])

def compress(S):
    '''Compresses using Run-Length encoding'''
    if S == "":
        return ""
    else:
        wNum = countWhite(S)
        if wNum >= 32:
            wNum = 31
        white = numToBinary(wNum)
        whiteBlock = "0"*(5-len(white)) + white

        if S[wNum:] == "":
            return whiteBlock
        
        bNum = countBlack(S[wNum:])
        if bNum >= 32:
            bNum = 31
        black = numToBinary(bNum)
        blackBlock = "0"*(5-len(black)) + black

        return whiteBlock + blackBlock + compress(S[wNum+bNum:])

def uncompress(S):
    '''Looks at 5 bit sections and converts them to that number of 0's or 1's'''
    if S == "":
        return ""
    elif len(S) == 5:
        return binaryToNum(S)*"0"
    return binaryToNum(S[0:5])*"0" + binaryToNum(S[5:10])*"1" + uncompress(S[10:])

'''
The largest number of bits that our compress algoithm would use to encode a 64 bit string
would be 325 bits because if it is alternating but starts with 1 it will return with 00000
followed by 00001 64 times
'''

def compression(S):
    '''
    Divides the compressed length by the uncompressed length to give the ratio
    ratio < 1: Reduced size
    ratio = 1: Same size
    ratio > 1: Greater size
    '''
    if S == "":
        return 1
    return len(compress(S))/len(S)

'''
We tested the given shape problems, as well as an all '0' and all '1' 10 bit string, and an
empty string. We also did some miscellaneous problems such as "101", "01", and "010101" which
should return 6.666..., 5, and 5 respectively.
'''

'''
Proffesor Lai can't be right because there is no way to ALWAYS shorten and shrink the
size of data. We can realize this by looking at all the possiblities there are. In a binary
64 bit string, there are 2^64 possible arrangements of the data. If Lai says that their
algortihm always shortens it, the size of the new compressed string would be at MOST 63 bits.
63 bits pf 1's and 0's give you 2^63 possible data arrangements. It is impossible to map 2^64
unique combinations to only 2^63 unique combinations, which would be needed to have an
algorithm that can shrink any string and then uncompress the shortened version.
'''

def testCompression():
    '''Tests compression() with 9 cases'''
    assert compression("0000000000") == .5
    assert compression("1111111111") == 1
    assert compression("101") == 6.666666666666667
    assert compression("01") == 5
    assert compression("010101") == 5
    assert compression("") == 1
    '''Penguin'''
    assert compression( "00011000"+"00111100"*3+"01111110"+"11111111"+"00111100"+"00100100") == 1.484375
    '''Smile'''
    assert compression("0"*8+"01100110"*2+"0"*8+"00001000"+"01000010"+"01111110"+"0"*8) == 1.328125
    '''Five'''
    assert compression("1"*9+"0"*7+"10000000"*2+"1"*7+"0"+"00000001"*2+"1"*7+"0") == 1.015625
