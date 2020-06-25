'''
Created on 10/10/2018
@author:   Susmitha Shailesh
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

'''settings for turtle'''
turtle.speed(0)
turtle.screensize(500,500, "orange")

turtle.pensize(200)
turtle.pencolor("red")
turtle.penup()
turtle.goto(-150,-100)
turtle.pendown()
turtle.circle(10)

turtle.pensize(150)
turtle.pencolor("yellow")
turtle.penup()
turtle.goto(-150,-100)
turtle.pendown()
turtle.circle(10)

turtle.pencolor("DarkOliveGreen")
turtle.pensize(200)
turtle.penup()
turtle.goto(-500,-250)
turtle.pendown()
turtle.forward(1000)

turtle.pencolor("brown")
turtle.left(90)
turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
turtle.pensize(5)

def sv_tree(trunk_length, levels):
    '''Draws a tree with inputs of initial trunk length and levels of branches'''
    if levels == 0:
        turtle.pencolor("green")
        turtle.circle(7)
        turtle.pencolor("brown")
        return
    
    turtle.forward(trunk_length)
    turtle.right(40)
    sv_tree(trunk_length/2, levels-1)
    turtle.left(40)
    turtle.backward(trunk_length)
    
    turtle.forward(trunk_length)
    turtle.left(40)
    sv_tree(trunk_length/2, levels-1)
    turtle.right(40)
    turtle.backward(trunk_length)

def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def fast_lucas_helper(n, memo):
        if n in memo:
            return memo[(n)]
        elif n == 0:
            return 2
        elif n == 1:
            return 1
        else:
            memo[(n)] = fast_lucas_helper(n-1, memo) + fast_lucas_helper(n-2, memo)
            return memo[(n)]
    return fast_lucas_helper(n, {})

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        elif amount == 0:
            return 0
        elif coins == ():
            return float("inf")
        elif coins[0] > amount:
            return fast_change_helper(amount, coins[1:],memo)
        else: 
            use = 1 + fast_change_helper(amount-coins[0], coins,memo)
            lose = fast_change_helper(amount, coins[1:],memo)
            memo[(amount, coins)] = min(use, lose)
            return memo[(amount, coins)]
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(128, 8)
