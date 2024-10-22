

# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
# Score 20

from collections import OrderedDict

def total_sales_by_product(num_items):
  products = OrderedDict()

  for _ in range(num_items):
    record = input().split()
    item_name = ' '.join(record[:-1])
    net_price = int(record[-1])
    
    if item_name in products:
      products[item_name] += net_price
    else:
      products[item_name] = net_price
    
  return products
   
def main():
  num_items = int(input())
  products = total_sales_by_product(num_items)
  
  for item_name, net_price in products.items():
    print(item_name, net_price) 
    
if __name__ == '__main__':
  main()  