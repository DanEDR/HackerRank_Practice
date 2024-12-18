

# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
# Score 20
import re

def fun(s):
    # return True if s is a valid email, else return False
    pattern = r'^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.fullmatch(pattern, s)) 
    

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)