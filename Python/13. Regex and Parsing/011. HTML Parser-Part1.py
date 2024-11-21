

# https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true
# Score 30

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print(f"Start :", tag)
    for attribute, value in attrs:
      print(f'-> {attribute} > {value}')

  def handle_endtag(self, tag):
    print(f"End   :", tag)
    
  def handle_startendtag(self, tag, attrs):
    print (f"Empty :", tag)
    for attribute, value in attrs:
      print(f'-> {attribute} > {value}')
    
if __name__ == '__main__':
  num_of_line = int(input())
  html_code = [input() for _ in range(num_of_line)]
  
  parser = MyHTMLParser()
  for html in html_code:
    parser.feed(html)