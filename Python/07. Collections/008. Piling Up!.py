

# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# Score 50

from collections import deque

def is_stackable(side_lengths):
  side_lengths = deque(side_lengths)
  last_piled = float('inf')
  
  while len(side_lengths) > 1:
    if side_lengths[0] >= side_lengths[-1]:
      current = side_lengths.popleft()
    else:
      current = side_lengths.pop()
      
    if last_piled < current:
      return 'No'
    
    last_piled = current
  
  return 'Yes'
  
  
if __name__ == '__main__':
  num_test_cases = int(input())

  for _ in range(num_test_cases):
    num_cubes = int(input())
    side_lengths = list(map(int, input().split()))
    
    print(is_stackable(side_lengths))
  