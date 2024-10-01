

# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Score 10

# Solution 1

def check_strict_superset():
  set_A = set(map(int, input().split()))
  number_of_other_sets = int(input())

  for _ in range(number_of_other_sets):
    set_B = set(map(int, input().split()))
    if not set_A.issuperset(set_B):
      return False
      
  return True
  
print(check_strict_superset())

# Solution 2

def check_strict_superset():
  set_A = set(map(int, input().split()))
  number_of_other_sets = int(input())
      
  return all(set_A.issuperset(set(map(int, input().split()))) for _ in range(number_of_other_sets))
  
print(check_strict_superset())