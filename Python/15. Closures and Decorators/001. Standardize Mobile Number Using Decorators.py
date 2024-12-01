

# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true
# Score 30

import re

mobile_number_pattern = re.compile(r'^(0|\+91|91)?(\d{5})(\d{5})$')

def wrapper(f):
    def fun(l):
        'We suppose that all numbers have a long equal or greater than 10'
        
        for i, num in enumerate(l):
          matches = mobile_number_pattern.match(num)
          l[i] = f'+91 {matches.group(2)} {matches.group(3)}'
        f(l)    
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 