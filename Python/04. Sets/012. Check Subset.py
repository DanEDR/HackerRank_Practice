

# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Score 10

def check_subset():
  number_of_test_cases = int(input())

  for _ in range(number_of_test_cases):
    number_of_elements_A = int(input())
    set_A = set(map(int, input().split()))
    number_elements_B = int(input())
    set_B = set(map(int, input().split()))
    
    print(set_A.issubset(set_B))
    
check_subset()