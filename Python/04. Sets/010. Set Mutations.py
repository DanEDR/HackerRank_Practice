

# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
# Score 10

def perform_set_operations():
  number_elements_A = int(input())
  set_A = set(map(int, input().split()))

  number_other_sets = int(input())
  for _ in range(number_other_sets):
    operation_name = input().split()
    set_B = set(map(int, input().split()))
    
    if operation_name[0] == 'update':
      set_A.update(set_B)
    elif operation_name[0] == 'intersection_update':
      set_A.intersection_update(set_B)
    elif operation_name[0] == 'difference_update':
      set_A.difference_update(set_B)
    else:
      set_A.symmetric_difference_update(set_B)
      
  return sum(set_A)