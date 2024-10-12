

# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Score 10

from itertools import product

list_A = list(map(int,input().split()))
list_B = list(map(int,input().split()))

for element in product(list_A, list_B):
  print(element, end=' ')