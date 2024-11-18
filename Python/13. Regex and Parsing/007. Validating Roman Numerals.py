

# https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true
# Score 20

import re

# Solution 1
regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

print(str(bool(re.match(regex_pattern, input()))))



# Solution 2
roman_regex_pattern = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')

def is_valid_roman(numeral):
    numeral = numeral.strip().upper()
    return bool(roman_regex_pattern.match(numeral))

if __name__ == '__main__':
    numeral = input() 
    print(is_valid_roman(numeral))