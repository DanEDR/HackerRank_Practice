

# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem?isFullScreen=true
# Score 30

def person_lister(f):
    def inner(people):
        people.sort(key= lambda person: int(person[2])) # person[2] -> age
        
        return list(map(f, people))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
