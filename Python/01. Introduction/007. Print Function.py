

# https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
# Score 20

def print_function(n):
  for i in range(1, n+1):
    print(i, sep="", end="")

if __name__ == '__main__':
    n = int(input())
    print_function(n)