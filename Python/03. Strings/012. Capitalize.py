

# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Score 20

def solve(s):
  capitalized = ''
  capitalized += s[0].upper() if s[0].isalpha() else s[0]
  
  for i in range(1,len(s)):
    capitalized += s[i].upper() if s[i-1] == ' ' and s[i].isalpha() else s[i]
    
  return capitalized