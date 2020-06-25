
#Susmitha Shailesh
#I pledge my honor that I have abided by the Stevens Honor System.

from cs115 import *

def knapsack(capacity, itemList):
    '''when given a maximum capacity and a list of items with a weight and
    a value, returns the maximum value of items without exceeding the capacity
    and a list of those items'''
    if capacity <= 0:
        return [0, []]
    elif itemList == []:
        return [0, []]
    elif itemList[0][0] > capacity:
        return knapsack(capacity, itemList[1:])
    else:
        use = knapsack(capacity-itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        if itemList[0][1] + use[0] > lose[0]:
            L = [itemList[0]] + use[1]
            return [itemList[0][1] + use[0], L]
        else: return lose

