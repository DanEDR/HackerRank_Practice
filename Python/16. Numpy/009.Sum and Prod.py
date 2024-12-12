

# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true
# Score 20

import numpy as np

def main():
    N, M = map(int, input().split())
    array = np.array([input().strip().split() for _ in range(N)], int)
    print(np.prod(np.sum(array, axis=0)))

if __name__ == '__main__':
    main()
