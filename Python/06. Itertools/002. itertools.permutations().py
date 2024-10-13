

# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Score 10

from itertools import permutations

string, permutation_size = input().split()
string = sorted(string) 
permutation_size = int(permutation_size)

for permutation in permutations(string, permutation_size):
  print(''.join(permutation))