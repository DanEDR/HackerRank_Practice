# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
# Score 30

from collections import Counter

def top_three_characters(s):
  s = sorted(s.lower())
  characters = Counter(s)
  return characters.most_common(3)

def print_top_three(s):
  top_three = top_three_characters(s)
    
  for character, value in top_three:
    print(character, value)

if __name__ == '__main__':
  s = input()
  print_top_three(s)