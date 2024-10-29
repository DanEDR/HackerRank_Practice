

# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
# Score 30

from datetime import datetime

# Complete the time_delta function below.

def time_delta(t1, t2):
  time_format = '%a %d %b %Y %H:%M:%S %z'
  
  dt1 = datetime.strptime(t1, time_format)
  dt2 = datetime.strptime(t2, time_format)
  
  diff_time = abs(dt1 - dt2).total_seconds()
  
  return str(int(diff_time))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()