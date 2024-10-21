

# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
# Score 20

from collections import defaultdict

def positions_of_occurrences(group_A, group_B):
    '''
    Devuelve las posiciones de las palabras en el group_A que aparecen en el group_B.
    
    :param group_A: Lista de palabras donde se buscarán las posiciones.
    :param group_B: Lista de palabras cuyas posiciones se desean encontrar.
    :return: Lista con las posiciones o -1 si no se encuentra la palabra.
    '''
    
    positions = defaultdict(list)

    for index, word in enumerate(group_A):
        positions[word].append(str(index + 1))

    results = []
    for word in group_B:
        if word in positions:
            results.append(' '.join(positions[word]))
        else:
            results.append('-1')

    return results
      
def main():
    group_A_size, group_B_size = map(int ,input().split())
    group_A = [input() for _ in range(group_A_size)]
    group_B = [input() for _ in range(group_B_size)]

    results = positions_of_occurrences(group_A, group_B)
    print('\n'.join(results))

if __name__ == '__main__':
    main()
  