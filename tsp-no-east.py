# Python2/3 script to implement traveling salesman problem using naive approach. 
from sys import maxsize 
import pprint
from copy import copy
from tabulate import tabulate

pp = pprint.PrettyPrinter(indent=4)
V = 11

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

  # store all vertex apart from source vertex 
  vertex = [] 
  for i in range(V): 
    if i != s: 
      vertex.append(i)

  # store minimum weight Hamiltonian Cycle 
  min_path = maxsize 

  while True: 

    # store current Path weight(cost) 
    current_pathweight = 0

    # compute current path weight 
    k = s 
    for i in range(len(vertex)): 
      current_pathweight += graph[k][vertex[i]] 
      k = vertex[i] 
    current_pathweight += graph[k][s] 

    # update minimum 
    min_path = min(min_path, current_pathweight) 

    if min_path == current_pathweight:
      min_vertex = copy(vertex)
      print(min_path, min_vertex)

    if not next_permutation(vertex): 
      break

  return min_path, min_vertex

# next_permutation implementation 
def next_permutation(L): 

  n = len(L) 

  i = n - 2
  while i >= 0 and L[i] >= L[i + 1]: 
    i -= 1

  if i == -1: 
    return False

  j = i + 1
  while j < n and L[j] > L[i]: 
    j += 1
  j -= 1

  L[i], L[j] = L[j], L[i] 

  left = i + 1
  right = n - 1

  while left < right: 
    L[left], L[right] = L[right], L[left] 
    left += 1
    right -= 1

  return True

# Driver Code 
if __name__ == "__main__": 

  # matrix representation of graph, in minutes of travel time:
  #
  # 0-alta
  # 1-arapahoe basin
  # 2-aspen snowmass
  # 3-big sky
  # 4-grand targhee
  # 5-jackson hole
  # 6-mammoth mountain
  # 7-snowbird
  # 8-squaw valley
  # 9-taos
  # 10-st. louis (update the last column for your city)
  #
  locations = ["alta", "a basin", "aspen snowmass", "big sky", "grand targhee", "jackson hole",\
    "mammoth mountain", "snowbird", "squaw valley", "taos", "st. louis"]
  graph = [\
  [0, 458,  402,  371,  299,  306,  532,  3,    520,   640,  1184],\
  [0, 0,    156,  667,  548,  502,  860,  559,  926,   302,  802],\
  [0, 0,    0,    687,  540,  494,  811,  400,  873,   405,  943],\
  [0, 0,    0,    0,    183,  212,  829,  377,  758,   946,  1314],\
  [0, 0,    0,    0,    0,    67,   741,  294,  668,   817,  1240],\
  [0, 0,    0,    0,    0,    0,    762,  305,  688,   769,  1192],\
  [0, 0,    0,    0,    0,    0,    0,    531,  214,   970,  1620],\
  [0, 0,    0,    0,    0,    0,    0,    0,    518,   636,  1183],\
  [0, 0,    0,    0,    0,    0,    0,    0,    0,     1103, 1680],\
  [0, 0,    0,    0,    0,    0,    0,    0,    0,     0,    918],\
  [0, 0,    0,    0,    0,    0,    0,    0,    0,     0,    0]]
  for i in range(len(graph)):
    for j in range(i):
      graph[i][j] = graph[j][i] # make graph undirected
  print(pp.pprint(graph))
  s = 10
  min_path, min_vertex = travellingSalesmanProblem(graph, s)
  min_vertex.append(s)
  min_vertex.insert(0, s)
  table = []
  for p_idx in range(1, len(min_vertex)):
    fromLocIdx = min_vertex[p_idx - 1]
    toLocIdx = min_vertex[p_idx]
    mins = graph[toLocIdx][fromLocIdx]
    hours = mins / 60.0
    table.append([locations[fromLocIdx], locations[toLocIdx], mins, hours])
  print(tabulate(table, ["from", "to", "mins", "hours"], tablefmt="grid"))
  print("%f total days driving" % (min_path / 60.0 / 24.0))


# This code is contributed by 
# sanjeev2552 
# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
#
# Modified by adwiens