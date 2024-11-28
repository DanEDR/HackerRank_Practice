

# https://www.hackerrank.com/challenges/validating-postalcode/problem?isFullScreen=true
# Score

import re

regex_integer_in_range = r"\d{6}"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?!(?:(?:(\d)(?=\1\d{4})|\d(\d)(?=\2\d{3})|\d{2}(\d)(?=\3\d{2})))\d{6})"	# Do not delete 'r'.


P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)