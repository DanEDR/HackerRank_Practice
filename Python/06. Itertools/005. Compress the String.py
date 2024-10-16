

# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Score 20

from itertools import groupby

input_string = input()

# Solution 1
for char, group in groupby(input_string):
    print((len(list(group)), int(char)), end=" ")


# Solution 2
occurrence_pair = [(len(list(group)), int(char)) for char, group in groupby(input_string)]

print(*occurrence_pair)