

# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
# Score 20

total_num = int(input())
list_of_num = input().split()

all_are_positive = all(int(num) > 0 for num in list_of_num)
any_is_palindromic = any(num == num[::-1] for num in list_of_num)

print(all_are_positive and any_is_palindromic)