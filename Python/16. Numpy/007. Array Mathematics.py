

# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
    N, M = map(int, input().split())
    array_A = np.array([input().split() for _ in range(N)], int)
    array_B = np.array([input().split() for _ in range(N)], int)

    print(array_A + array_B,
          array_A - array_B,
          array_A * array_B,
          array_A // array_B,
          array_A % array_B,
          array_A ** array_B,
          sep='\n')

if __name__ == '__main__':
    main()

