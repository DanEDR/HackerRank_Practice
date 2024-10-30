

# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
# Score 20

import re

def is_valid_regex(pattern):
  try:
    re.compile(pattern)
    return True
  except re.error:
    return False
  
if __name__ == '__main__':
  num_of_test = int(input())
  
  for _ in range(num_of_test):
    string = input()
    print(is_valid_regex(string))