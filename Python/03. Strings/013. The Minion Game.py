

# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Score 40

def minion_game(string):
  # your code goes here
  vowels = 'AEIOU'
  kevin_score, stuart_score = 0, 0
  
  for i in range(len(string)):
    if string[i] in vowels:
      kevin_score += len(string) - i
    else:
      stuart_score += len(string) - i
  
  if stuart_score < kevin_score:
    print(f'Kevin {kevin_score}')
  elif stuart_score > kevin_score:
    print(f'Stuart {stuart_score}')
  else:
    print('Draw')