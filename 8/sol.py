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
for i in range(1, rows-1):
  for j in range(1, cols-1):
    tree = arr[i,j]
    right = np.max(arr[i,j+1:])
    left = np.max(arr[i,:j])
    top = np.max(arr[:i,j])
    down = np.max(arr[i+1:,j])
    # print(tree, right)
    if tree>right or tree > left or tree > top or tree > down:
      #print(f"to {tree} einai visible")
      visible += 1

answer1 = outer_trees + visible
print("part 1:", answer1)
