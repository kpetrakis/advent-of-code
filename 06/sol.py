#!/usr/bin/env python
from collections import deque

data = open("input.txt", "r").read()#.readlines()
data = data.strip('\n')
# print(data)

sop_marker = -1 # start of packet marker position
som_marker = -1 # start of message marker position
l = deque() # list holding the 4 most recent letters
message_l = deque() # list holding the 14 most recent letters
for i, letter in enumerate(data):
  l.append(letter)
  message_l.append(letter)

  # find packet marker
  if len(l) == 4:
    s = set(l)
    if len(s) == 4:
      # found it
      sop_marker = i + 1 # account for zero indexing
    else:
      l.popleft()

  # find message marker
  if len(message_l) == 14:
    s = set(message_l)
    if len(s) == 14:
      # found it
      som_marker = i + 1 # account for zero indexing
    else:
      message_l.popleft()

print("sop marker:", sop_marker)
print("som marker:", som_marker)
