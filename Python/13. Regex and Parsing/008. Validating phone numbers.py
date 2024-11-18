

# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
# Score 20

import re

pattern = re.compile(r'^[789]\d{9}$')

def is_valid_mobile(number):
  return 'YES' if pattern.match(number) else 'NO'
  
if __name__ == '__main__':
  number_of_inputs = int(input())
  for _ in range(number_of_inputs):
    mobile_num = input()
    print(is_valid_mobile(mobile_num))