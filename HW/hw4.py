
#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *

def rowSums(L):
    if len(L) == 2:
        return [L[0]+L[1]]
    else: return [L[0]+L[1]] + rowSums(L[1:])

def pascal_row(n):
    if n < 0:
        return "error"
    elif n == 0:
        return [1]
    elif n == 1:
        return [1,1] 
    else: return [1] + rowSums(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    if n < 0:
        return "error"
    elif n == 0:
        return [[1]]
    else: return pascal_triangle(n-1) + [pascal_row(n)]
    
def test_pascal_row():
    assert pascal_row(-20) == "error"
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(3) == [1,3,3,1]
    assert pascal_row(10) == [1,10,45,120,210,252,210,120,45,10,1]

def test_pascal_triangle():
    assert pascal_triangle(-50) == "error"
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1],[1,1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],\
                                  [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
