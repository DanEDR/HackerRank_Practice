

# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
# Score 10

# Solution 1

def count_substring(string, sub_string):
  len_sub_string = len(sub_string)
  count = sum(1 if string[i:i+len_sub_string] == sub_string else 0 
  for i in range(len(string))) 

  return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# Solution 2

def count_substring(string, sub_string):
  len_sub_string = len(sub_string)
  count = 0
  
  for i in range(len(string)):
   if string[i:i+len_sub_string] == sub_string:
    count += 1
  return count