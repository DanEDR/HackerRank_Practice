

# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
# Score 10

def main():
  number_of_elements = int(input())
  set_s = set(map(int, input().split()))
  number_of_commands = int(input())

  for _ in range(number_of_commands):
    value = input().split()
    command = value[0]

    if command == 'pop' : 
      set_s.pop()
    elif command == 'remove':
      set_s.remove(int(value[1]))
    else:
      set_s.discard(int(value[1]))

  print(sum(set_s))
  
if __name__ == '__main__':
  main()
