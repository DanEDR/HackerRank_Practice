

# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
# Score 10

from itertools import combinations

string_S, size = input().split()
size = int(size)
string_S = sorted(string_S)

# Solution 1

for i in range(1, size + 1):
  for combination in combinations(string_S, i):
    print(''.join(combination))
    
# Solution 2

for i in range(1, size + 1):
  print(*map(''.join, combinations(string_S, i)), sep='\n')