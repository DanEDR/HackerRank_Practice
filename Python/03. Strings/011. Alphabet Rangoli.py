

# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
# Score 20
def print_rangoli(size):
    
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size):
      left = ''.join(abc[size-1-j].ljust(2,'-') for j in range(i))
      right = left[::-1]
      print((left + abc[size-1-i] + right).center(4*size - 3,'-'))

    for i in range(size-2,-1,-1):
      left = ''.join(abc[size-1-j].ljust(2,'-') for j in range(i))
      right = left[::-1]
      print((left + abc[size-1-i] + right).center(4*size - 3,'-'))