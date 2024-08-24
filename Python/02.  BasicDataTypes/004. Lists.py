

# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
# Score 10

# version 1 
if __name__ == '__main__':
    result = []
    N = int(input())
    for _ in range(N):
     values = input().split()
     if values[0] == 'insert':
      result.insert(int(values[1]), int(values[2]))
     elif values[0] == 'print':
      print(result)
     elif values[0] == 'remove':
      result.remove(int(values[1]))
     elif values[0] == 'append':
      result.append(int(values[1]))
     elif values[0] == 'sort':
      result.sort()
     elif values[0] == 'pop':
      result.pop()
     else:
      result.reverse()
      
# version 2

operations = {
    'insert': lambda x, y: result.insert(x, y),
    'print': lambda: print(result),
    'remove': lambda x: result.remove(x),
    'append': lambda x: result.append(x),
    'sort': lambda: result.sort(),
    'pop': lambda: result.pop(),
    'reverse': lambda: result.reverse()
}

def process_operation(values):
    operations[values[0]](*[int(x) for x in values[1:]])

def process_input():
    N = int(input())
    for _ in range(N):
        process_operation(input().split())

if __name__ == '__main__':
    result = []
    process_input()