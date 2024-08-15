

# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true
# Score 10

def generate_coordinates_excluding_sum(x, y, z, n):
    return [[i, j, k] for i in range(x + 1) 
                          for j in range(y + 1) 
                          for k in range(z + 1) 
                          if i + j + k != n]

if __name__ == '__main__':
    # Get the four inputs from the user
    x, y, z, n = (int(input()) for _ in range(4))
    print(generate_coordinates_excluding_sum(x, y, z, n))