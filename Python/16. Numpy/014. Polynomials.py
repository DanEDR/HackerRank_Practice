

# https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
  coefficients = list(map(float, input().split()))
  value = float(input())

  print(np.polyval(coefficients, value))

if __name__ == '__main__':
  main()
