#!/usr/bin/env python
from collections import defaultdict, deque

data = open('input.txt', 'r').read().rstrip().split('\n')

path = deque() # stack of directories - the most recent on top
sizes = {} # {dir: size} for every dir
for line in data:
  if line == '$ cd ..':
    path.pop()
  elif line.startswith('$ cd'):
    d = line.split(' ')[2] # dir name
    if path:
      path.append("".join([path[-1], d]))
    else: # if it is empty just add the root dir /
      path.append(line.split(' ')[2])

    sizes[path[-1]] = 0 # init dict

  elif line.split(' ')[0].isnumeric():
    size = int(line.split(' ')[0]) # file size
    for d in path:
      # add the file size to every dir in path
      sizes[d] += size

  # print(path)
  # print(sizes)

answer1 = sum(v for v in sizes.values() if v <= 100000)
print("answer part 1: ", answer1)

# part 2
free_space = 70000000 - max(v for v in sizes.values())
space_to_go = 30000000 - free_space
# print(free_space)
# print(space_to_go)

answer2 = min(v for v in sorted(sizes.values()) if v >= space_to_go)
print("answer part 2: ", answer2)
