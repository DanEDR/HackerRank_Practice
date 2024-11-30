

# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem?isFullScreen=true
# Score 20

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    
    for child in elem:
      new_depth = depth(child, level)
      maxdepth = max(new_depth, maxdepth)
      
    return level

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)