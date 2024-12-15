

# https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
  N = int(input())
  array_A = np.array([input().split() for _ in range(N)], int)
  array_B = np.array([input().split() for _ in range(N)], int)

  print(np.dot(array_A, array_B))

if __name__ == '__main__':
  main()
