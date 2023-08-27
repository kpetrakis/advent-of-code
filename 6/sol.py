#!/usr/bin/env python
from collections import deque

data = open("input.txt", "r").read()#.readlines()
data = data.strip('\n')
# print(data)

sop_marker = -1 # start of packet marker position
l = deque() # list holding the 4 most recent letters
for i, letter in enumerate(data):
  l.append(letter)

  if len(l) == 4:
    s = set(l)
    if len(s) == 4:
      # found it
      sop_marker = i + 1 # account for zero indexing
    else:
      l.popleft()

print("answer:", sop_marker)
