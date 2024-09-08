

# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Score 40

# Solution 1

def merge_the_tools(string, k):
  
    for i in range(0,len(string),k):
      sub_str = ''
      for j in range(k):
        if string[i+j] not in sub_str:
          sub_str += string[i+j]
      print(sub_str)

# Solution 2

def merge_the_tools(string, k):
  
  for i in range(0,len(string),k):
    dic = {string[i+j] : j  for j in range(k)}
    print(''.join(dic))  