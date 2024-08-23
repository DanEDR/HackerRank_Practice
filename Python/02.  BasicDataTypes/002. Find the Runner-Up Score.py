

# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
# Score 10

def runner_up_score(n, arr):
    max_score = max(arr)
    arr = list(set(arr))
    arr.remove(max_score)
    return max(arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(runner_up_score(n, arr))