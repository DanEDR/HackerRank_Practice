

# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
# Score 10


def names_with_second_lowest_grade(students_records):
  # Create a list of unique scores
  unique_scores = list({student[1] for student in students_records})
  # Find the second lowest score
  second_lowest_score = sorted(unique_scores)[1]
    
  # Retrieve names of students with the second lowest score
  second_lowest_names = sorted(student[0] for student in students_records 
                         if student[1] == second_lowest_score)
    
  for name in second_lowest_names:
   print(name)


if __name__ == '__main__':
    students_records = []
    for _ in range(int(input())):
     name = input()
     score = float(input())
     students_records.append([name, score])
        
    names_with_second_lowest_grade(students_records)