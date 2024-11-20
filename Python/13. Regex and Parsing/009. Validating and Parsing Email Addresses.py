

# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true
# Score 20

import re

pattern = re.compile(r'^<[A-Za-z][\w\-\.]+@[A-Za-z]+\.[A-Za-z]{1,3}>$')

def is_valid_email(string):
  return bool(pattern.match(string))
    
if __name__ == '__main__':
  num_of_emails = int(input())

  for _ in range(num_of_emails):
    name, email = input().split()
    
    if is_valid_email(email):
      print(f'{name} {email}')