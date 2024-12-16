

# https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
  array_A = np.array(input().split(), int)
  array_B = np.array(input().split(), int)

  print(
    np.inner(array_A, array_B),
    np.outer(array_A, array_B),
    sep='\n'
  )

if __name__ == '__main__':
  main()
