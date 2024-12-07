#!/usr/bin/env python
from collections import deque
from collections.abc import Sequence

class Rope(Sequence):
  def __init__(self, num_of_knots):
    self.knots = list() # head is first tail is last
    for _ in range(num_of_knots):
      self.knots.append(Knot(0, 0))

  def __getitem__(self, i):
    return self.knots[i]

  def __len__(self):
    return len(self.knots)

  def __repr__(self):
    return f"rope({len(self.knots)}): {self.knots}"

  def adjust(self):
    """
    traverse the knots list and adjust every pair of knots to follow each other
    """
    for index1, index2 in zip(range(len(self)), range(1, len(self))):
      #print(f"adjust {index2}")
      #print(f"before adjust: {self.knots[index2]}") 
      dist = (self.knots[index1].i - self.knots[index2].i, self.knots[index1].j - self.knots[index2].j)
      absdist = (abs(self.knots[index1].i - self.knots[index2].i), abs(self.knots[index1].j - self.knots[index2].j))
      touching = (absdist[0] == 0 and absdist[1]==0) or (absdist[0]<=1 and absdist[1] <=1) 
      if not touching:
        if dist[1] > 1 and dist[0] == 0:
          #print("R")
          self.knots[index2].move('R')
        elif dist[1] < -1 and dist[0] == 0:
          #print("L")
          self.knots[index2].move('L')
        elif dist[0] > 1 and dist[1] == 0:
          #print("D")
          self.knots[index2].move('D')
        elif dist[0] < -1 and dist[1] == 0:
          #print("U")
          self.knots[index2].move('U')
        elif (dist[0] < -1 and dist[1] >= 1) or (dist[1] > 1 and dist[0] <= -1):
          # UR
          #print("UR")
          self.knots[index2].move('UR')
        elif dist[0] < -1 and dist[1] <= -1 or (dist[1] <-1 and dist[0] <= -1):
          # UL 
          #print("UL")
          self.knots[index2].move('UL')
        elif (dist[0] > 1 and dist[1] >= 1) or (dist[1]>1 and dist[0] >=1):
          # DR 
          #print("DR")
          self.knots[index2].move('DR')
        elif (dist[0] > 1 and dist[1] <= -1) or (dist[1] < -1 and dist[0] >= 1):
          # DL
          #print("DL")
          self.knots[index2].move('DL')
      #print(f"after adjust: {self.knots[index2]}") 
    #print("-------------------------------")

class Knot:
  def __init__(self, i, j):
    #self.pos = (i, j) # (row, col)
    self.i = i # row
    self.j = j # col

  def move(self, direction):
    assert direction in ['R', 'L', 'U', 'D','UL', 'UR', 'DL', 'DR']
    if direction == 'R':
      self.j += 1
    if direction == 'L':
      self.j -= 1
    if direction == 'D':
      self.i += 1
    if direction == 'U':
      self.i -= 1
    if direction == 'UL':
      self.i -= 1
      self.j -= 1
    if direction == 'UR':
      self.i -= 1
      self.j += 1
    if direction == 'DL':
      self.i += 1
      self.j -= 1
    if direction == 'DR':
      self.i += 1
      self.j += 1

  def __repr__(self):
    return "Knot(" + str((self.i, self.j)) + ")"

data = open("input.txt", 'r').readlines()
data = [d.strip('\n') for d in data]
# print(data)

tail_positions = set() # the positions visited by tail
rope = Rope(10)
head = rope[0]
tail = rope[-1]
for row in data:
  direction, count = row[0], row[2:]
  #tail_positions.add((tail.i, tail.j))

  for c in range(int(count)):
    # print(f"head moved {direction}")
    head.move(direction)

    rope.adjust()
    tail_positions.add((tail.i, tail.j))

# print("final rope:", rope)

answer2 = len(tail_positions) 
print("part 2 answer: ", answer2)
