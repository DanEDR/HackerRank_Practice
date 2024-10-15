

# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
# Score 10

from itertools import combinations_with_replacement

string, size = input().split()
size = int(size)
string = sorted(string)

print(*map("".join,combinations_with_replacement(string, size)), sep="\n")