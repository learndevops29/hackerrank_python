#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
def sockMerchant(n, ar):
    sum = 0
    s1 = []     
    for i in ar:
        if i not in s1:     
            s1.append(i)   # genrating list with unique value ( removed duplicate) 
    for j in s1:
        sum = sum + ar.count(j) // 2    # now running loop on uique value list to original list to count count and if it is divided by 2 take it result for sum 
    return sum
    #####################################################
    #sum([ar.count(i)//2 for i in set(ar)])  on liner solution 
    ##########################################################
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #3fptr.close()

"""
PROBLEM STATEMENT 
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example


There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

int n: the number of socks in the pile
int ar[n]: the colors of each sock
Returns

int: the number of pairs
Input Format

The first line contains an integer , the number of socks represented in .
The second line contains  space-separated integers, , the colors of the socks in the pile.

Constraints

 where 
Sample Input

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
Sample Output

3
Explanation

sock.png

There are three pairs of socks.
"""