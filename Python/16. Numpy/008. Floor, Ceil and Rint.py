

# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true
# Score 20

import numpy as np

np.set_printoptions(legacy='1.13')

if __name__ == '__main__':
  array = np.array(input().split(), float)

  print(
    np.floor(array),
    np.ceil(array),
    np.rint(array),
    sep='\n'
  )
