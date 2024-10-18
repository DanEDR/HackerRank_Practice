

# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
# Score 50

from itertools import product

def main():
  K, M = map(int, input().split())

  element_lists = [list(map(int, input().split()))[1:] for _ in range(K)]

  max_mod_sum = 0

  for combination in product(*element_lists):
    sum_of_squares = sum(x**2 for x in combination) % M
    max_mod_sum = max(max_mod_sum, sum_of_squares)

  print(max_mod_sum)
  
if __name__ == '__main__':
  main()
