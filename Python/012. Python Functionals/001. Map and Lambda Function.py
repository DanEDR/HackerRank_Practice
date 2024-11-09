

# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
# Score 20

cube = lambda x: x ** 3 

def fibonacci(n):
  # return a list of fibonacci numbers
  last, current = 0, 1
  sequence = [last, current]

  for _ in range(2, n):
    last, current = current, last + current
    sequence.append(current)
  
  return sequence[:n] if n <= 2 else sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))