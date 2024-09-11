

# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Score 50

def calculate_happiness_score(array, A, B):
  
  happiness_score = 0
  
  for integer in array:
    if integer in A:
      happiness_score += 1
    elif integer in B:
      happiness_score -= 1
  
  return happiness_score
  
if __name__ == "__main__":
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
  A = set(map(int, input().split()))
  B = set(map(int, input().split()))
  print(calculate_happiness_score(array, A, B))