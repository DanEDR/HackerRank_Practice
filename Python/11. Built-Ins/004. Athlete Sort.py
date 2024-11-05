

# https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
# Score 30

def sort_spreadsheet(k, arr):
  sorted_indices = sorted(range(len(arr)), key=lambda i: arr[i][k])
  new_arr = [arr[i] for i in sorted_indices]

  return new_arr

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    # Print the spreadsheet sorted
    for record in sort_spreadsheet(k, arr):
      print(*record)