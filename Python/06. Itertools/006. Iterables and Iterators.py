

# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
# Score 40

from itertools import combinations

list_length = int(input())
list_elements = sorted(input().split())
subseq_length = int(input())

favorable_outcomes = 0
total_outcomes = 0

for combination in combinations(list_elements, subseq_length):
    if combination[0] == 'a':
        favorable_outcomes += 1
    total_outcomes += 1

probability = favorable_outcomes / total_outcomes
print(probability)