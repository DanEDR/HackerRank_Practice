

import numpy

# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true
# Score 20

if __name__ == '__main__':
  list_of_integers = list(map(int, input().split()))
  array_of_integers = numpy.array(list_of_integers)
  
  print(numpy.reshape(array_of_integers, (3,3)))
