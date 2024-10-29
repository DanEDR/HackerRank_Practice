

# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
# Score 10

def division(a, b):
  try:
    result = int(a) // int(b)
    print(result)
  except (ZeroDivisionError, ValueError) as e:
    print('Error Code:', e)

if __name__ == '__main__':
  test_cases = int(input())
  
  for _ in range(test_cases):
    a, b = input().split()
    division(a, b)