#Susmitha Shailesh
#Working with Rohan Rao
#I pledge my honor that I have abided by the Stevens Honor System

import sys
from cs115 import map, reduce, filter

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scoreList):
    '''returns the corresponding score of letter in scoreList'''
    if scoreList[0] == []:
        return none
    elif scoreList[0][0] == letter:
        return scoreList[0][1]
    else:
        return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    '''returns the sum of the scores of the letters in S'''
    if S == '':
        return 0
    else:
        return letterScore(S[0], scoreList) + wordScore(S[1:], scoreList)

def remove(e, word):
    '''everytime an element in L is equal to e, skip it when returning back the list'''
    if word == "":
        return ""
    elif word[0] == e:
        return word[1:]
    else:
        return word[0] + remove(e, word[1:])

def checkWord(letters, word):
    '''checks if all of the letters in word can be found in list letters'''
    if word == "":
        return True
    elif letters == []:
        return False
    elif letters[0] in word:
        return True * checkWord(letters[1:] , remove(letters[0],word))
    else: return checkWord(letters[1:], word)

def addScore(word):
    '''Takes a word and returns an array with the word and it's score'''
    return [word, wordScore(word, scrabbleScores)] 

def scoreList(Rack):
    '''filters out the words that can't be made then pairs the words with their score'''
    return map(addScore, filter(lambda word: checkWord(Rack, word), Dictionary))

def bigger(x,y):
    '''compares the second element of two arrays and returns the larger array'''
    if x[1]> y[1]:
        return x
    else:
        return y

def bestWord(Rack):
    '''Uses scoreList and bigger function to determine the best word and it's score'''
    if scoreList(Rack) == []:
        return ['',0]
    else:
        return reduce(bigger, scoreList(Rack))
