

# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Score 10

def count_unique_students():
  number_students_english = int(input())
  students_english = set(map(int, input().split()))

  number_students_french = int(input())
  students_french = set(map(int, input().split()))

  total_number_students = students_english.symmetric_difference(students_french)
  return len(total_number_students)

print(count_unique_students())