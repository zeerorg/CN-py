"""

Every router has it's own array
each array has elements equal to number of routers
at initialization the distance of router to itself will be 0
input all the edges and input those in vector of each router
create a neighbour table from input in previous step
keep supplying tables to each other, and stop when all tables don't change in the next iteration

"""

def start():
  print("Number of nodes: {}\nAll neighbours: {}".format(4, [(0, 1, 3), (1, 3, 4), (2, 3, 3), (0, 2, 2) ]))
  print("Routes: {}".format(main()[1]))

def main(edges=[(0, 1, 3), (1, 3, 4), (2, 3, 3), (0, 2, 2) ], num=4):
  """
  num = number of routers
  edges = array of tuples of three elements example: [ (0, 1, 3), (1, 3, 4), (2, 3, 3), (0, 2, 2) ]
  """

  # initialize routers array
  routers = []
  for x in range(num):
    routers.append([1000] * num)
    routers[x][x] = 0
  
  # set distance to all neighbours 
  for edge in edges:
    routers[edge[0]][edge[1]] = edge[2]
    routers[edge[1]][edge[0]] = edge[2]

  start_table = routers.copy()

  flag = True
  while flag:
    upflag = False
    for nbrs in edges:
      routers[nbrs[0]], up_flag1 = update_table(routers[nbrs[0]], routers[nbrs[1]], dist=nbrs[2])
      routers[nbrs[1]], up_flag2 = update_table(routers[nbrs[1]], routers[nbrs[0]], dist=nbrs[2])
      upflag = upflag or up_flag1 or up_flag2

    flag = upflag

  return start_table, routers


def update_table(vec1, vec2, dist):
  """
  This function takes the routing vector and the neighbours routing vector and updates the current vector.
  If there is no update the second value is returned as false, else second value is True
  vec1 = vector to update
  vec2 = vector which is received
  dist = distance between them

  """
  flag = False

  for router_to in range(len(vec1)):
    if vec1[router_to] > vec2[router_to] + dist:
      vec1[router_to] = vec2[router_to] + dist
      flag = True

  return vec1, flag

start()
