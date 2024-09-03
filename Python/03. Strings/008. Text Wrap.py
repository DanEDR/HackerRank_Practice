

# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# Score 10

# Solution 1
import textwrap

def wrap(string, max_width):
  
 return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
 string, max_width = input(), int(input())
 result = wrap(string, max_width)
 print(result)
 
# Solution 2

def wrap(string, max_width):
 wrap_list = [string[i:i+max_width] for i in range(0,len(string),max_width)]
 return '\n'.join(wrap_list)