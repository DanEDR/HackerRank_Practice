

# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
# Score 10

def avg_score(total_subjects, all_subjects):    
  avg_scores = [sum(scores) / total_subjects for scores in zip(*all_subjects)]
  return avg_scores

if __name__ == '__main__':
  total_students, total_subjects = map(int,input().split())
  
  all_subjects = []
  for _ in range(total_subjects):
    subject = list(map(float, input().split()))
    all_subjects.append(subject)
  
  print(*avg_score(total_subjects, all_subjects), sep='\n')