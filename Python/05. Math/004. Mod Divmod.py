

# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true
# Score 10

a = int(input())
b = int(input())

print(a//b, a % b, divmod(a,b), sep='\n')