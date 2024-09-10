

# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
# Score 10

def average(array):

    distinct_heights = set(array)
    average = "{:.3f}".format(sum(distinct_heights) / len(distinct_heights))
    return average