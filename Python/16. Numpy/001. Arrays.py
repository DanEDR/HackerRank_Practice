

# https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true
# Score 20

import numpy

def arrays(arr):
    arr = numpy.array(arr, float)
    return arr[::-1]

if __name__ == '__main__':
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)
