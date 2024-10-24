

# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
# Score 20

from collections import deque

methods = {
  'append' : lambda x: d.append(x),
  'pop': lambda: d.pop(),
  'popleft' : lambda: d.popleft(),
  'appendleft' : lambda x: d.appendleft(x)
}

def process_operation(values):
  methods[values[0]](*[int(x) for x in values[1:]])

def process_input():
  num_operations = int(input())

  for _ in range(num_operations):
    value = input().split()
    process_operation(value)
    

if __name__ == '__main__':
  d = deque()
  process_input()
  print(*d)