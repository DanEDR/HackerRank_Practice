

# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
# Score 20

from collections import namedtuple

def average_mark():
  num_students = int(input())
  Student = namedtuple('Student', input().split())
  
  total_mark = 0

  for _ in range(num_students):
    student_data = input().split()
    student = Student(*student_data)
    total_mark += int(student.MARKS)
    
  average_mark = total_mark / num_students
  return average_mark
  
if __name__ == '__main__':
  print(f'{average_mark():.2f}')