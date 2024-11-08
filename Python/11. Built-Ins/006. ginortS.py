

# https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
# Score 40

'''
This function to sort a string in the following manner:

- All sorted lowercase letters are ahead of uppercase letters.
- All sorted uppercase letters are ahead of digits.
- All sorted odd digits are ahead of sorted even digits.
'''

# Solution 1
def sorted_string(string):
  l_letters, u_letters = [], []
  odd_digits, even_digits = [], []

  for character in string:
    if character.islower():
      l_letters.append(character)
    elif character.isupper():
      u_letters.append(character)
    elif character.isdigit() and int(character) % 2 != 0:
      odd_digits.append(character)
    else:
      even_digits.append(character)

  l_letters.sort()
  u_letters.sort()
  odd_digits.sort()
  even_digits.sort()

  sorted_string = l_letters + u_letters + odd_digits + even_digits

  return "".join(sorted_string)

# Solution 2

def sorted_string_2(string):
  characters = list(string)
  (
    characters
    .sort(
      key=lambda x: (
        x.isdigit() and int(x) % 2 == 0,
        x.isdigit(),
        x.isupper(),
        x
      )
    )
  )
  
  return ''.join(characters)
  
if __name__ == '__main__':
  s = input()
  
  print(sorted_string(s))