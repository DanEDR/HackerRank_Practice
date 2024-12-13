

# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
  row, col = map(int, input().split())
  array = np.array([input().split() for _ in range(row)], int)

  print(np.max(np.min(array, axis=1)))

if __name__ == '__main__':
  main()
