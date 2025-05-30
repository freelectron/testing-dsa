#!/bin/python3

import math
import os
import random
import re
import sys

def gridChallenge(grid):
    #[[0]] * len(grid[0]) # reference to the same object [0]
    out = [ [0] for _ in range(len(grid[0])) ]   # creates a new object [0] for every iteration
    for row in grid: 
        raw_ascii_list = sorted(list(map(ord, row))) 
        for i_col, ch_ord in enumerate(raw_ascii_list):
            if ch_ord >= out[i_col][-1]:
                # out[i_col] = out[i_col] + [ch_ord] # this is inefficient because out[i_col] is reassigned to a new list copy evertime
                out[i_col].append(ch_ord) # inplace adding
            else:
                print(row, " ", out, " ", out[i_col][-1], "vs", ch_ord)
                return "NO"
    
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()


##################################################################################

def doSum(s:str) -> str:
    s = str(sum(list(map(int,s))))
    if len(s)>1:
        print(s)
        doSum(s)
    else:
        print("o: ", s)
        return s

def superDigit(n, k):
    s = n*k
    out = doSum(s)
    print(out)
    return int(out)
    
    
def superDigit1(n, k):    
    s = n*k
    # sum the digits 
    while len(s) > 1:
        s = str(sum(list(map(int,s))))
    
    return int(s)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



######################################################################################

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    n_bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            return "Too chaotic"
        
        # Only check up to 2 people ahead of current position
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                n_bribes += 1

    return n_bribes

    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
