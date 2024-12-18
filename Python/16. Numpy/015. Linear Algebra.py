

# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
  N = int(input())
  matrix = np.array([input().split() for _ in range(N)], float)

  print(round(np.linalg.det(matrix), 2))

if __name__ == '__main__':
  main()
