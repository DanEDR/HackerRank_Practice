

# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
# Score 10

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    hash_value = hash(t)
    print(hash_value)