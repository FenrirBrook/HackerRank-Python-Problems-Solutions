import math
import os
import random
import re
import sys


def plusMinus(arr):

    positives = 0
    negatives = 0
    zeros = 0

    for ele in arr:
        if ele > 0:
            positives += 1
        elif ele < 0:
            negatives += 1
        elif ele == 0:
            zeros += 1

    print(round(positives/len(arr),6))
    print(round(negatives/len(arr),6))
    print(round(zeros/len(arr),6))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)