import math
import os
import random
import re
import sys
import time

def timeConversion(s):
    return time.strftime('%H:%M:%S', time.strptime(s, '%I:%M:%S%p'))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    # fptr.write(result + '\n')
    # fptr.close()
    print(result)