
# https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=true
# Score 10

def square_funtion (n):
  for i in range(n):
    print(i ** 2)

if __name__ == '__main__':
    n = int(input())
    square_funtion(n)