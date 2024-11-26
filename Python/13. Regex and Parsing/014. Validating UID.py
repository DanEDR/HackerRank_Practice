

# https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=true
# Score 30

import re 

pattern = re.compile(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})[A-Za-z0-9]{10}$')


def is_valid_UID(string):
  return 'Valid' if pattern.match(string) else 'Invalid'
  
if __name__ == '__main__':
  num_of_test = int(input())
  
  for _ in range(num_of_test):
    UID = input()
    print(is_valid_UID(UID))