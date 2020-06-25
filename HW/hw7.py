#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

def numToBaseB(N, B):
    '''takes as input a non-negative integer N and a base B and
    returns a string representing the number N in base B'''
    if N == 0:
        return ""
    def nTBB(N, B):
        if N == 0:
            return "0"
        else: return nTBB(N//B, B) + str(N%B)
    return nTBB(N, B)

def baseBToNum(S, B):
    '''takes as input a string S and a base B where S represents a
    number in base B '''
     def BToN(S, n, acc):
        if S == "":
            return acc
        else:
            return BToN(S[:-1], n+1, acc + (int(S[-1]))*(B**n))
     return BToN(S, 0, 0)

def baseToBase(B1, B2, SinB1):
    '''takes three inputs: a baseB1, a baseB2 and SinB1, which is a string
    representing a number in baseB1 and returns a string
    representing the same number in baseB2'''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S, T):
    '''takes two binary strings S and T as input and returns their sum,
    also in binary'''
    numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

FullAdder ={ ('0','0','0') : ('0','0'),\
             ('0','0','1') : ('1','0'),\
             ('0','1','0') : ('1','0'),\
             ('0','1','1') : ('0','1'),\
             ('1','0','0') : ('1','0'),\
             ('1','0','1') : ('0','1'),\
             ('1','1','0') : ('0','1'),\
             ('1','1','1') : ('1','1') }

def addB(S, T):
    '''takes two binary strings S and T as input and returns their sum,
    also in binary using FullAdder'''
    def addB_helper(S, T, cin, acc):
        if S == "" and T == "":
            return cin + acc
        elif S == "":
            tup = FullAdder['0', T[-1], cin]
            return addB_helper('', T[:-1], tup[1], tup[0]+acc)
        elif T == "":
            tup = FullAdder[S[-1], '0', cin]
            return addB_helper(S[:-1], '', tup[1], tup[0]+acc)
        else:
            tup = FullAdder[S[-1], T[-1], cin]
            return addB_helper(S[:-1], T[:-1], tup[1], tup[0]+acc)
    ans=addB_helper(S, T, '0', '')
    if ans[0] == "0":
        ans = ans[1:]
    return ans
