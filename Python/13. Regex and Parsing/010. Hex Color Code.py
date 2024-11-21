

# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
# Score 30

import re

pattern = re.compile(r'[: ](#[A-Fa-f0-9]{3,6})')

def is_valid_hex_color(code):
  matches = pattern.findall(code)
  return matches if matches else None

if __name__ == '__main__':
  num_code_line = int(input())
  
  for _ in range(num_code_line):
    code = input()
    valid_hex_colors = is_valid_hex_color(code)
    
    if valid_hex_colors:
      print(*valid_hex_colors, sep='\n')