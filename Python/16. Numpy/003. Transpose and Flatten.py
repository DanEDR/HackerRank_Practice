

# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true
# Score 20

import numpy


if __name__ == '__main__':
  row, column = map(int, input().split())
  matrix = [input().split() for _ in range(row)]
  my_matrix = numpy.array(matrix, int)
  
  print(numpy.transpose(my_matrix))
  print(my_matrix.flatten())
