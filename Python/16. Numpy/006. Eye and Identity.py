

# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true
# Score 20

import numpy as np

np.set_printoptions(legacy='1.13')

if __name__ == '__main__':
  row, column = map(int, input().split())

  matrix = np.array(np.eye(row, column))
  print(matrix)
