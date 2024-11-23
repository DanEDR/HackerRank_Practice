

# https://www.hackerrank.com/challenges/html-parser-part-2/problem?isFullScreen=true
# Score 30

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  
  def handle_data(self, data):
    if data != '\n':
      print('>>> Data', data, sep='\n')
    
  def handle_comment(self, data):
    if '\n' in data:
      print(f'>>> Multi-line Comment', data, sep='\n')
    else:
      print(f'>>> Single-line Comment', data, sep='\n')
  
  
if __name__ == '__main__':
  html = ""       
  for i in range(int(input())):
      html += input().rstrip()
      html += '\n'
    
  parser = MyHTMLParser()
  parser.feed(html)
  parser.close()