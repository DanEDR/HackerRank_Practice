# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
# Score 10

def weird(n):
  if n % 2 != 0:
    print('Weird')
  elif n % 2 == 0 and 2 <= n <= 5 :
    print('Not Weird')
  elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
  else:
    print('Not Weird')

if __name__ == '__main__':
    n = int(input().strip())
    weird(n)