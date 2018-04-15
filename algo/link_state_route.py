"""
GET a list of all edges in the graph
Calculate all neighbours from that list using a dict, every node is a key
Create an LSDB using those edges.
apply algorithm from forouzan pg 606
"""

from functools import reduce

def start():
  print("Number of nodes: {}\nAll neighbours: {}".format(4, [(0, 1, 3), (1, 3, 4), (2, 3, 3), (0, 2, 2) ]))
  print("LSDB: {}\nAll distance vectors: {}".format(*main()))

def main(edges=[(0, 1, 3), (1, 3, 4), (2, 3, 3), (0, 2, 2) ], num=4):
  """
  """
  neighbours = {}
  for edge in edges:
    if neighbours.get(edge[0]) == None:
      neighbours[edge[0]] = []
    if neighbours.get(edge[1]) == None:
      neighbours[edge[1]] = []
    neighbours[edge[0]].append(edge[1])
    neighbours[edge[1]].append(edge[0])


  """
  Creating LSDB:
  1.  add a new list for every node.
  2.  for x against y check:
      2.1 if x == y: add "0"
      2.2 if x is neighbour of y: give dist(x, y)
      2.3 else 1000
  """
  LSDB = []
  for x in range(num):
    link = []
    for y in range(num):
      if x == y:
        link.append(0)
      elif y in neighbours[x]:
        link.append(get_neighbour_dist(x, y, edges))
      else:
        link.append(1000)
    LSDB.append(link)

  """
  Book algo starts
  """
  D = []
  for node in range(num):
    d_vec = list(LSDB[node])
    tree = set([node])
    while tree.__len__() != num:
      min_nbr = None
      for nbr in range(num):
        if nbr not in tree and (min_nbr == None or LSDB[node][min_nbr] > LSDB[node][nbr]):
          min_nbr = nbr
      for nbr_nbr in neighbours[min_nbr]:
        if nbr_nbr not in tree:
          d_vec[nbr_nbr] = min(d_vec[nbr_nbr], d_vec[min_nbr] + LSDB[min_nbr][nbr_nbr])
      tree.add(min_nbr)
    D.append(d_vec)

  return LSDB, D


def get_neighbour_dist(x, y, edges):
  """
  Takes edges returns distance between neighbours
  """
  return list(filter(lambda edge: (edge[0] == x and edge[1] == y) or (edge[0] == y and edge[1] == x), edges))[0][2]


start()
