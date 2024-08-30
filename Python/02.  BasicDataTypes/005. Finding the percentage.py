

# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# Score 10


def avg_print(student_marks, query_name):
  avg_score = sum(student_marks[query_name])/3
  return print("{:.2f}".format(avg_score))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_print(student_marks, query_name)