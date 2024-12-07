#!/usr/bin/env python
import numpy as np

data = open('input.txt', 'r').read().rstrip().split('\n')

l = [] # list to create arr from
for i, line in enumerate(data):
  row = []
  for number in line:
    row.append(int(number))
  l.append(row)

arr = np.array(l, dtype=np.int32)
assert arr.ndim == 2, "dims are false"
rows, cols = arr.shape
#total = arr.size
outer_trees = rows + (cols-1) + (rows-1) + (cols-2)
visible = 0
max_scenic_score = 0 # part2
for i in range(1, rows-1):
  for j in range(1, cols-1):
    tree = arr[i,j]
    right = arr[i,j+1:]
    left = arr[i,:j]
    top = arr[:i,j]
    down = arr[i+1:,j]
    if tree>np.max(right) or tree > np.max(left) or tree > np.max(top) or tree > np.max(down):
      #print(f"to {tree} einai visible")
      visible += 1
    
    if np.where(right>=tree)[0].size > 0:
      right_vis = min(np.where(right>=tree)[0]) + 1
    else:
      right_vis = right.shape[0]
    if np.where(left>=tree)[0].size > 0:
      left_vis = j - max(np.where(left>=tree)[0])
    else:
      left_vis = left.shape[0]
    if np.where(down>=tree)[0].size > 0:
      down_vis = min(np.where(down>=tree)[0]) + 1
    else:
      down_vis = down.shape[0]
    if np.where(top>=tree)[0].size > 0:
      top_vis = i - max(np.where(top>=tree)[0])
    else:
      top_vis = top.shape[0]

    if (right_vis * left_vis * top_vis * down_vis) > max_scenic_score:
      max_scenic_score = right_vis * left_vis * top_vis * down_vis

answer1 = outer_trees + visible
answer2 = max_scenic_score
print("part 1:", answer1)
print("part 2:", answer2)
