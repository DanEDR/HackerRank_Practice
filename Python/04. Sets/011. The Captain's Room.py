

# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
# Score 10

size_group = int(input())
elements = list(map(int, input().split()))

room_numbers = set(elements)

for room in room_numbers:
  elements.remove(room)
  if room not in set(elements):
    print(room)