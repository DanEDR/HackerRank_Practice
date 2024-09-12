

# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Score 10

def symmetric_difference_order(a, b):
  difference = a.symmetric_difference(b)
  
  return sorted(difference)


if __name__ == "__main__":
  M = int(input())
  a = set(map(int, input().split()))
  N = int(input())
  b = set(map(int, input().split()))
  
  result = symmetric_difference_order(a, b)
  print('\n'.join(map(str, result)))
