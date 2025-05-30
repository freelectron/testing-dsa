
import math
import os
import random
import re
import sys

from collections import Counter as c


def lonelyinteger(a):
    seen_once = list()
    seen_twice = list()
    for el in a:
        if el in seen_once:
            seen_twice.append(el)
        else: 
            seen_once.append(el)
    
    return  (set(seen_once) - set(seen_twice)).pop()

def lonelyinteger(a):
    a_bag = c(a)    
    for k,v in a_bag.items():
        if v == 1:
            return k

# Most efficient 
def lonelyinteger(a):
    result = 0
    for num in a:
        res_prev = result
        # you are pretty much switching on and off bits that you have seen, and because you are as if you are storing everything in the bit's format, 
        # you do not need additional spaces and only simple checks (which are bitwise xor opertars)
        # you can use this since there is only one unique! 
        result = result ^ num
        print(res_prev," ", num, " - ", result)

    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())
    # a = list(map(int, input().rstrip().split()))

    result = lonelyinteger([1,2,3,4,3,2,1])

    fptr.write(str(result) + '\n')

    # fptr.close()

##########################################################

def diagonalDifference(arr):
    # n := # rows = m := # col 
    # Elements on the main diag: i = j
    # Elements on the other diag: j = m - s ; i = s where s = i
    n = len(arr)
    m = len(arr[0])
    main_diag = 0 
    not_main_diag = 0 
    for i in range(n):
        for j in range(m):
            if i == j:
                main_diag+=arr[i][j]
            if m - i - 1 == j:
                not_main_diag+=arr[i][j]  
                
    return abs(main_diag - not_main_diag)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)


##########################################################

def countingSort(arr):
    freq_arr = [0] * 100
    for el in arr: 
        freq_arr[el] += 1
    
    return freq_arr
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

