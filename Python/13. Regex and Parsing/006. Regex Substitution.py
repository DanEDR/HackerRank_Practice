

# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
# Score 20

import re

#Solution 1
def replace(match):
  if match.group(1) == '&&':
    return 'and' 
  elif match.group(1) == '||':
    return 'or'

def modify_text(text):
  pattern = r'(?<= )(&&|\|\|)(?= )'
  return re.sub(pattern, replace, text)

#Solution 2
pattern = re.compile(r'(?<= )(&&|\|\|)(?= )')

replacement_map = {
  '&&': 'and',
  '||': 'or'
}

def modify_text_2(text):
  return pattern.sub(lambda match: f'{replacement_map[match.group(1)]}', text)

if __name__ == '__main__':
  num_of_lines = int(input())
  
  for _ in range(num_of_lines):
    line = input()
    print(modify_text(line))