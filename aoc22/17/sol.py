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
N = 1_000_000_000_000 # 2022
rested = 0
floor_idx = 0
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
        stopped_rock = rock # points where rock landed
        blocked.update(rock)
        max_y = max((y for (x, y) in blocked))
        stopped = True
        rested += 1
      else:
        rock = tuple((x, y+dy) for (x,y) in rock)

  '''
  Code used to find repeated pattern....
  Will run for years, just used to find the equation for Part 2.
  '''
  # code used to find pattern
  changed_floor = False
  for y in set(y for (x,y) in stopped_rock):
    if all([(x,y) in blocked or (x, y+1) in blocked for x in range(7)]):
      floor_idx = y
      changed_floor = True
    elif all([(x,y) in blocked or (x, y-1) in blocked for x in range(7)]):
      floor_idx = y - 1
      changed_floor = True
  if changed_floor:
    print(f"new floor idx = {floor_idx:4} rested {rested:3} with max_y {max_y:4} new height {max_y-floor_idx}")
    blocked = set(filter(lambda t: t[1]>=floor_idx, blocked))

  # Just print some to debug
  if rested >= 2000:
    break

print(f"Part 1: {max_y}")
print(f"Part 2: {320 + ((N-202) // 1720)*2704 + 1955}")

'''
@Part 2 explained:
at first 202 rested stones I get height: 320
After that we get a patter of 2704 increase in height / 1720 rested rocks.
(N-202) // 1720 times the pattern repeats
(N-202) % 1720 remaining stones we need to counter for. The height here increases
by 1955
'''