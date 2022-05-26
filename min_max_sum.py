import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    max = 0
    min = 0
    for i in range(len(arr)):
        aux = sum(arr) - arr[i]
        if max < aux:
            max = aux
        if min > aux or min == 0:
            min = aux
    print(min, max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)