

# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
# Score 20

import re

def position_matches(string, substring):
  positions = []
  start = 0
  
  while True:
    match = re.search(substring, string[start: ])
    if not match:
      break
  
    start_index = start + match.start()
    end_index = start + match.end() - 1
    positions.append((start_index, end_index))
    start += match.start() + 1
    
  return positions if positions else [(-1, -1)]

if __name__ == '__main__':
  string = input()
  substring = input()
  
  print(*position_matches(string, substring), sep='\n')