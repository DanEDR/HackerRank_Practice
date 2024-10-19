

# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# Score 10

from collections import Counter

def total_sales(shoe_sizes, num_costomers):
  inventory = Counter(shoe_sizes)
  total_revenue = 0

  for _ in range(num_costomers):
    shoe_size, price = map(int, input().split())
    
    # Varificar si hay inventario disponible
    if inventory.get(shoe_size, 0) > 0:
      total_revenue += price
      inventory[shoe_size] -= 1

  return total_revenue

def main():
  num_shoes = int(input())
  shoe_sizes = list(map(int, input().split()))
  num_costomers = int(input())
  
  # Calcular y mostrar los ingresos totales
  print(total_sales(shoe_sizes, num_costomers))
  

if __name__ == '__main__':
  main()