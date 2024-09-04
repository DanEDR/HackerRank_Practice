

# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
# Score 10

def print_formatted(number):
    
    n = len(bin(number)[2:])
    for i in range(1, number+1):
      print(str(i).rjust(n), end = ' ')
      print(oct(i)[2:].rjust(n), end = ' ')
      print(hex(i)[2:].upper().rjust(n), end = ' ')
      print(bin(i)[2:].rjust(n))
    