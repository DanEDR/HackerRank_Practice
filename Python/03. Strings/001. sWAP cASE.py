

#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
# Score 10

# Solution 1
def swap_case(s):
  convert_s = ''
  for letter in s:
    if letter.islower():
      convert_s += letter.upper()
    else:
      convert_s += letter.lower()
  
  return convert_s

# Solution 2

def swap_case(s):
    
  converted_string = "".join(letter.upper() if letter.islower() else letter.lower() for letter in s)
  return converted_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)