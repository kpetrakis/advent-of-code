#!/usr/bin/env python
from collections import deque

def parse(filename):
  lines = [line.strip() for line in open(filename, 'r').readlines()]
  return lines

def elevation(ch):
  if ch == "S":
    return elevation('a')
  elif ch == "E":
    return elevation('z')
  else:
    return ord(ch) - ord('a')

def create_graph():
  graph = {}
  for i, line in enumerate(lines):
    for j, char in enumerate(line):
      pos = (i, j)
      neighbor_pos = [(i + di, j + dj) for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                   if len(lines) > i+di >= 0 and len(line) > j+dj >= 0]

      children = set()
      for x, y in neighbor_pos:
        if elevation(lines[x][y]) - elevation(char) <= 1:
          children.add((x, y))

      graph[pos] = children
  return graph

def bfs(graph, root, dst):
  # level of dst node running BFS with root start, will equal the fewest steps to reach dst 
  level = {k: None for k in graph.keys()} # level of node in BFS traverse
  marked = {k: False for k in graph.keys()} # used for calculating the level

  # run BFS
  # root = start
  visited, queue = set(), deque()
  queue.append(root)
  visited.add(root)

  level[root] = 0
  marked[root] = True

  while queue:
    v = queue.popleft()

    if v == dst:
      # dst reached
      break

    # if not visitied, mark visited
    for neighbor in graph[v]:
      if neighbor not in visited:
        if not marked[neighbor]:
          level[neighbor] = level[v] + 1 # steps required to reach node
          marked[neighbor] = True
        visited.add(neighbor)
        queue.append(neighbor)

  return level[v]

lines = parse('input.txt')
# get pos of start S and dst E
for i, line in enumerate(lines):
  if 'S' in line:
    start = (i, line.index('S')) # zero indexed - row, col
  if 'E' in line:
    dst = (i, line.index('E')) # zero indexed - row, col

graph = create_graph()
answer1 = bfs(graph, start, dst)
print("part 1:", answer1)
