#!/usr/bin/env python3
import itertools

def parse(filename):
  return itertools.cycle(open(filename, 'r').read().strip())

jets_gen = parse('input.txt') # jets of hot gas movement '<' or '>'

# ksekinaw tin arithmisi apo katw aristera!
rock1 = ((2,1), (3,1), (4,1), (5,1))
rock2 = ((3,1), (2,2), (3,2), (4,2), (3,3))
rock3 = ((2,1), (3,1), (4,1), (4,2), (4,3))
rock4 = ((2,1), (2,2), (2,3), (2,4))
rock5 = ((2,1), (3,1), (2,2), (3,2))
rock_gen = itertools.cycle([rock1, rock2, rock3, rock4, rock5]) # cycle through that

# can't move past those points - but can be in exactly those pts
blocked = set()
max_y = 0 
print("initial pos:", [(p[0], p[1]+ max_y + 3) for p in rock1])
N = 2022
rested = 0
#for i in range(N):
while rested < N:
  rock = next(rock_gen)
  rock = tuple((p[0], p[1]+max_y+3) for p in rock) # inital rock pos
  # print("rock appeared:", rock)

  stopped = False
  vertical_move = True
  while not stopped:# and c<8:
    if vertical_move:
      vertical_move = False
      dx = 1 if next(jets_gen) == '>' else -1
      #print(f"horizontal move {dx}")
      if max((x+dx for (x,y) in rock)) <= 6 and min((x+dx for (x,y) in rock)) >= 0 and not blocked.intersection(set((x+dx, y) for (x,y) in rock)):
        rock = tuple((x+dx, y) for (x, y) in rock)
    else:
      vertical_move = True
      #print("verical(falling) move")
      dy = -1
      if (min(y+dy for (x,y) in rock)) < 1 or blocked.intersection(set((x, y+dy) for (x,y) in rock)):
        #print("move didn't happen. I am already in floor and stopped")
        blocked.update(rock)
        max_y = max((y for (x, y) in blocked))
        stopped = True
        rested += 1
      else:
        rock = tuple((x, y+dy) for (x,y) in rock)

print(f"Part 1: {max_y}")

# ANSWER 3191