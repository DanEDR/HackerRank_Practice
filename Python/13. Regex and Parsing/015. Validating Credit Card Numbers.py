

# https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
# Score 40

import re 

pattern = re.compile(r'^(?!.*(.)(-?\1){3,}.*)([456][0-9]{3}-?)([0-9]{4}-?){3}$')

def is_valid_credit_card(card_number):
  return 'Valid' if pattern.match(card_number) else 'Invalid'

if __name__ == '__main__':
  number_test = int(input())
  
  for _ in range(number_test):
    card_number = input()
    print(is_valid_credit_card(card_number))
  