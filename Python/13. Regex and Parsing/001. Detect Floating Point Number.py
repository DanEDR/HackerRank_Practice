

# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
# Score 20

import re


def is_float(value):
  requirements = r'^[+-]?\d*\.\d+?$'
  return bool(re.fullmatch(requirements, value))
  

if __name__ == '__main__':
  num_of_test_cases = int(input())
  
  for _ in range(num_of_test_cases):
    string = input()
    print(is_float(string))