#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

import sys
import random

def createBoard(width, height):
    '''creates a new array with specified width and height'''
    board = []
    for i in range(height):
        row = []
        for c in range(width):
            row = row + [0]
        board = board + [row]
    return board

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )

    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    """ creates an empty board and then modifies it
    so that all cells except the ones on the border are "on"
    """
    A = createBoard( w, h )

    for row in range(1,h-1):
        for col in range(1,w-1):
                A[row][col] = 1
    return A

def randomCells(w,h):
    """returns an array of randomly assignmed 1's and 0's except that
    the other edge of the array is completely empty"""
    A = createBoard(w,h)
    
    for row in range(1,h-1):
        for col in range(1,w-1):
                A[row][col] = random.choice([0,1])
    return A

def copy(A):
    ''' makes a deep copy of A'''
    B = createBoard(len(A[0]),len(A))

    for row in range(len(A)):
        for col in range(len(A[0])):
                B[row][col] = A[row][col]

    return B

def innerReverse(A):
    '''makes a deep copy of A and switches every value within B except
    those on the edge'''
    B = copy(A)

    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if A[row][col] == 1:
                B[row][col] = 0
            else:
                B[row][col] = 1

    return B

def countNeighbors(row,col,A):
    '''counts how many of the neighboring cells of A[row][col] are "alive"'''
    count = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if A[r][c] == 1:
                count= count + 1
    if A[row][col] == 1:
        return count-1
    else: return count
                

def next_life_generation(A):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    newA = copy(A)

    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if countNeighbors(row,col,A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row,col,A) > 3:
                newA[row][col] = 0
            elif countNeighbors(row,col,A) == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]

    return newA


