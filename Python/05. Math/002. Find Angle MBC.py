

# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
# Score 10

import math

def round_well(number):
  
  if number - math.floor(number) < 0.5:
    return math.floor(number)
  return math.ceil(number)


def angle_MBC(opposite_legs, adjacent_legs):
  
  theta = math.atan(opposite_legs / adjacent_legs)
  theta_degrees = math.degrees(theta)
  
  return round_well(theta_degrees)
  
if __name__ == "__main__":
  opposite_legs = float(input()) #length of side AB
  adjacent_legs = float(input()) #length of side BC
  
  print(f"{angle_MBC(opposite_legs, adjacent_legs)}\u00B0")
  
  
  #Help https://en.wikipedia.org/wiki/Thales%27s_theorem#:~:text=In%20geometry,%20Thales's%20theorem%20states%20that
  