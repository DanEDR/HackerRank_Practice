

# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Score 50

from collections import Counter

def count_words(num_words):
  words = [input() for _ in range(num_words)]
  word_count = Counter(words)
  
  return word_count

def main():
  num_words = int(input())
  word_count = count_words(num_words)
  
  print(len(word_count))
  print(*[value for value in word_count.values()])
   
if __name__ == '__main__':
  main()