import math
import os
import random
import re
import sys


## inefficient 
def miniMaxSum(arr):
    arr = sorted(arr) # time O(n logn) space O(n)
    print(sum(arr[:-1]), sum(arr[1:]))

## efficient 
def miniMaxSum2(arr):
    arr_max = max(arr) # n
    arr_min = min(arr) # n
    arr_sum = sum(arr) # <n

    print( arr_sum - arr_max, arr_sum - arr_min)

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)


####################################################################

import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0 
    neg = 0 
    zero = 0 
    for i in arr:
        if i > 0:
            pos+=1
        elif i < 0:
            neg+=1
        else:
            zero+=1
    
    n_arr = len(arr)
    
    print(pos / n_arr)
    print(neg / n_arr)
    print(zero / n_arr)


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)


