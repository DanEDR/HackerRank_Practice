

# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Score 10

def door_mat(n, m):
 for i in range( n//2):
  print(('.|.'*(2*i+1)).center(m,'-'))
  
 print('WELCOME'.center(m,'-'))

 for i in range(n//2, 0, -1):
  print(('.|.'*(2*i-1)).center(m,'-'))
  
if __name__ == '__main__':
 # note m = 3*n
 n, m = input().split()
 door_mat(int(n), int(m))