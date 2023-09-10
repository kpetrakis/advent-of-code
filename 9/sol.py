#!/usr/bin/env python
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

head = Knot(0, 0)
tail = Knot(0, 0)
tail_positions = set() # the positions visited by tail
for row in data:
  direction, count = row[0], row[2:]
  tail_positions.add((tail.i, tail.j))

  for c in range(int(count)):
    # print(f"head moved {direction}")
    head.move(direction)

    dist = (head.i - tail.i, head.j - tail.j)
    absdist = (abs(head.i - tail.i), abs(head.j - tail.j))
    touching = (absdist[0] == 0 and absdist[1]==0) or (absdist[0]<=1 and absdist[1] <=1) 
    if not touching:
      if dist[1] > 1 and dist[0] == 0:
        #print("R")
        tail.move('R')
      elif dist[1] < -1 and dist[0] ==0:
        #print("L")
        tail.move('L')
      elif dist[0] > 1 and dist[1] == 0:
        #print("D")
        tail.move('D')
      elif dist[0] < -1 and dist[1] == 0:
        #print("U")
        tail.move('U')

      elif (dist[0] < -1 and dist[1] == 1) or (dist[1] > 1 and dist[0]==-1):
        # UR
        #print("UR")
        tail.move('UR')
      elif dist[0] < -1 and dist[1] == -1 or (dist[1] <-1 and dist[0] == -1):
        # UL 
        #print("UL")
        tail.move('UL')
      elif (dist[0] > 1 and dist[1] == 1) or (dist[1]>1 and dist[0] ==1):
        # DR 
        #print("DR")
        tail.move('DR')
      elif (dist[0] > 1 and dist[1] == -1) or (dist[1] < -1 and dist[0] == 1):
        # DL
        #print("DL")
        tail.move('DL')

    tail_positions.add((tail.i, tail.j))
     
    # print("head:", head)
    # print("tail:", tail)

answer1 = len(tail_positions) 
print("part 1 answer: ", answer1)
