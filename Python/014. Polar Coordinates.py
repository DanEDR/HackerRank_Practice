

# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
# Score 10

import cmath

complex_number = complex(input())

modulus = abs(complex_number)
phase = cmath.phase(complex_number)

print(modulus, phase, sep = "\n")