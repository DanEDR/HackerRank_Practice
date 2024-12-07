

# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true
# Score 20

import numpy



if __name__ == '__main__':
  N, M, P = map(int, input().split())

  array_NxP = numpy.array([input().split() for _ in range(N)], int)
  array_MxP = numpy.array([input().split() for _ in range(M)], int)

  print(numpy.concatenate((array_NxP, array_MxP), axis=0))
