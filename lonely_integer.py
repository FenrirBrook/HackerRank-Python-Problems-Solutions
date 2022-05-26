# Given an array of integers, where all elements but one occur twice, find the unique element.
# Example
# The unique element is .
from enum import unique
import math
import os
import random
import re
import sys


def lonelyinteger(a):
    
    unique = None
    a_unique = set(a)
    for i in a_unique:
        count = 0
        for j in a:
            if i == j:
                count += 1
            if count > 1:
                break
        if count == 1:
            unique = i    
    return unique
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()