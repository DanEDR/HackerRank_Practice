

# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true
# Score 20

import re

def matched_substrings(string):
  pattern = r'(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOU])'
  matches = re.findall(pattern, string)
  
  return matches if matches else [-1]

if __name__ == '__main__':
  string = input()
  
  print(*matched_substrings(string), sep='\n')