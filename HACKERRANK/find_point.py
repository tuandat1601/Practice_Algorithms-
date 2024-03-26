# https://www.hackerrank.com/challenges/find-point/problem?isFullScreen=true
import math
import os
import random
import re
import sys
def findPoint(px, py, qx, qy):
    # Write your code here
    return qx+(qx - px),qy+(qy-py) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        px = int(first_multiple_input[0])

        py = int(first_multiple_input[1])

        qx = int(first_multiple_input[2])

        qy = int(first_multiple_input[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()