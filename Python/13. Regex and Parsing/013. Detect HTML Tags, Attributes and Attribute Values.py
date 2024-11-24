

# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true
# Score 30

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print(tag)
    for atrribute, value in attrs:
        print(f'-> {atrribute} > {value}')
        
if __name__ == '__main__':
  parser = MyHTMLParser()
  
  num_of_lines = int(input())
  for _ in range(num_of_lines):
    html = input()
    parser.feed(html)
    
  parser.close()