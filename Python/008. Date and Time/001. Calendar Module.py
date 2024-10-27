

# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
# Score 10

import calendar

def day_of_week(year, month, day):
  weekday = calendar.weekday(year, month, day)
  
  print(calendar.day_name[weekday].upper())
  
if __name__ == '__main__':
  month, day, year = map(int, input().split())
  day_of_week(year, month, day)