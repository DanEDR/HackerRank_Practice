

# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
  row, col = map(int, input().split())
  array = np.array([input().strip().split() for _ in range(row)], dtype=int)

  print(np.mean(array, axis=1))
  print(np.var(array, axis=0))
  print(round(np.std(array, dtype=np.float64), 11))

if __name__ == '__main__':
  main()
