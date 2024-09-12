

# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true
# Score 10

def main():
  total_number_country = int(input())
  name_country = set()
  
  for _ in range(total_number_country):
    country = input()
    name_country.add(country)
  
  total_unique_countries = len(name_country)
  print(total_unique_countries)

if __name__ == "__main__":
  main()