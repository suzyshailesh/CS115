'''
Rohan Rao working with Susmitha Shailesh
I pledge my honor that I have abided by the Stevens Honor System
'''
from cs115 import *

class Board():

    def __init__(self, width=7, height=6):
        self.__width = width
        self.__height = height
        self.__board = self.createBoard()

    def createOneRow(self):
        """Returns one rows of zeros of width "width"...  """
        row = []
        for col in range(self.__width):
            row += [' ']
        return row

    def createBoard(self):
        '''Returns "height" rows with width "width"'''
        A = []
        for row in range(self.__height):
            A += [self.createOneRow()]
        return A

    def __str__(self):
        '''returns string of board'''
        display = ''
        for row in range(self.__height):
            display += '|'
            for col in range(self.__width):
                display += self.__board[row][col]
                display += '|'
            display += '\n'
        for col in range(self.__width*2+1):
            display += '-'
        display += '\n'
        for col in range(self.__width):
            display += ' ' + str(col)    
        return display

    def allowsMove(self,col):
        '''checks to be sure thatcis within the range from 0 to the last
        column and make sure that there is still room left in the column'''
        if col in range(self.__width):
            if self.__board[0][col] == ' ':
                return True
        return False

    def addMove(self, col, ox):
        '''adds ox checker to column col'''
        if self.allowsMove(col):
            for row in range(self.__height-1,-1,-1):
                if self.__board[row][col] == ' ':
                    self.__board[row][col] = ox
                    break
        

    def setBoard(self, moveString):
        """takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'

        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers"""
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsDel(self, col):
        '''checks if column has any moves'''
        if col in range(self.__width):
            if self.__board[self.__height-1][col] != ' ':
                return True
        return False
    
    def delMove(self, col):
        '''deletes last move in column'''
        if self.allowsDel(col):
            for row in range(self.__height):
                if self.__board[row][col] != ' ':
                    self.__board[row][col] = ' '
                    break

    def winsFor(self, ox):
        '''checks to see if player ox has won horizontally, vertically, or
        diagonally'''
        consec = 0
        '''Horizontal'''
        for row in range(self.__height):
            for col in range(self.__width):
                if self.__board[row][col] == ox:
                    consec += 1
                    if consec == 4:
                        return True
                else: consec = 0
        '''Vertical'''
        for col in range(self.__width):
            for row in range(self.__height):
                if self.__board[row][col] == ox:
                    consec += 1
                    if consec == 4:
                        return True
                else: consec = 0
        '''Up+Right vertical check'''
        for row in range(3,self.__height):
            tempRow = row
            for col in range(self.__width):
                if self.__board[tempRow][col] == ox:
                    consec += 1
                    if consec == 4:
                        return True
                else:
                    consec = 0
                tempRow -= 1
                if tempRow < 0:
                    break
        '''Up+Right horizontal check'''
        for col in range(1, self.__width-3):
            tempCol = col
            for row in range(self.__height-1,0,-1):
                if self.__board[row][tempCol] == ox:
                    consec += 1
                    if consec == 4:
                        return True
                else:
                    consec = 0
                tempCol += 1
                if tempCol == self.__width:
                    break
        '''Down+Right vertical check'''
        for row in range(self.__height-3):
            tempRow = row
            for col in range(self.__width):
                if self.__board[tempRow][col] == ox:
                    consec += 1
                    if consec == 4:
                        return True
                else:
                    consec = 0
                tempRow += 1
                if tempRow == self.__height:
                    break
        '''Down+Right horizontal check'''
        for col in range(3, self.__width):
            tempCol = col
            for row in range(self.__height-1,0,-1):
                if self.__board[row][tempCol] == ox:
                    consec += 1
                    if consec == 4:
                        return True
                else:
                    consec = 0
                tempCol -= 1
                if tempCol == 0:
                    break
        return False

    def hostGame(self):
        '''plays game'''
        print("Let's play Connect Four!")
        print(self)

        while True:
            xMove = int(input('X\'s move:'))
            self.addMove(xMove, 'X')
            print(self)

            if self.winsFor('X'):
                print('Player X wins!')
                break

            oMove = int(input('O\'s move:'))
            self.addMove(oMove, 'O')
            print(self)

            if self.winsFor('O'):
                print('Player O wins!')
                break
