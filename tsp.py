# Python3 program to implement traveling salesman 
# problem using naive approach. 
from sys import maxsize 
import pprint
from copy import copy
pp = pprint.PrettyPrinter(indent=4)
V = 13

# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s): 

  # store all vertex apart from source vertex 
  vertex = [] 
  for i in range(V): 
    if i != s: 
      vertex.append(i) 
  print(vertex)

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
  # 9-sugarbush
  # 10-sugarloaf
  # 11-taos
  # 12-st. louis (update the last column for your city)
  #
  graph = [[0, 458, 402, 371, 299, 306, 532, 3, 520, 2100, 2220, 640, 1184],\
  [0, 0, 156, 667, 548, 502, 860, 559, 926, 1800, 1920, 302, 802],\
  [0, 0, 0, 687, 540, 494, 811, 400, 873, 1920, 2040, 405, 943],\
  [0, 0, 0, 0, 183, 212, 829, 377, 758, 2160, 2220, 946, 1314],\
  [0, 0, 0, 0, 0, 67, 741, 294, 668, 2160, 2280, 817, 1240],\
  [0, 0, 0, 0, 0, 0, 762, 305, 688, 2100, 2220, 769, 1192],\
  [0, 0, 0, 0, 0, 0, 0, 531, 214, 2580, 2700, 970, 1620],\
  [0, 0, 0, 0, 0, 0, 0, 0, 518, 2100, 2220, 636, 1183],\
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 2580, 2700, 1103, 1680],\
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 275, 1980, 1077],\
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2100, 1216],\
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 918],\
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
  print(len(graph))

  for i in range(len(graph)):
    for j in range(i):
      graph[i][j] = graph[j][i] # make graph undirected
  print(pp.pprint(graph))
  s = 12
  print(travellingSalesmanProblem(graph, s)) 

# This code is contributed by 
# sanjeev2552 
# https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
#
# Modified by adwiens