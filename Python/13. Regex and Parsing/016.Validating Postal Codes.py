

# https://www.hackerrank.com/challenges/validating-postalcode/problem?isFullScreen=true
# Score 80

import re

regex_integer_in_range = r"[1-9]\d{5}"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?!(?:(\d)(\d)\1\2\d\d|\d(\d)(\d)\3\4\d|\d\d(\d)(\d)\5\6|(\d)\d\7(\d)\d\8))(?=.*(\d).\9.*)"	# Do not delete 'r'.


P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)