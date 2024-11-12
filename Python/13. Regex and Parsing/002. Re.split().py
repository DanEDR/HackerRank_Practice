

# https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true
# Score 20

import re

regex_pattern = r"\D"	

print("\n".join(re.split(regex_pattern, input())))