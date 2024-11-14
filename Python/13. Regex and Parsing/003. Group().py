

# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
# Score 20

import re

def first_character_repeating(string):
  pattern = r'([a-zA-Z0-9])\1+'
  repeated_characters = re.search(pattern, string)
  
  return repeated_characters.group(1) if repeated_characters else -1

if __name__ == '__main__':
  string = input()
  
  print(first_character_repeating(string))