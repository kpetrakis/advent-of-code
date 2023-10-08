#!/usr/bin/env python3

def parse(filename):
  with open(filename, 'r') as f:
    lines =  [line.strip() for line in f.readlines()]
    rocks = set() # the pos where rocks are placed
    for line in lines:
      points = [tuple(map(int, coords.split(','))) for coords in line.split(' -> ')]
      for i, point in enumerate(points[1:], start=1):
        dx = point[0] - points[i-1][0] 
        dy = point[1] - points[i-1][1]
        if dx:
          stepx = dx // abs(dx)
          for xcoord in range(points[i-1][0], point[0] + stepx, stepx):
            rocks.add((xcoord, point[1]))
        if dy:
          stepy = dy // abs(dy)
          for ycoord in range(points[i-1][1], point[1] + stepy, stepy):
            rocks.add((point[0], ycoord))

  return rocks

rocks = parse('input.txt')

def part1():
  count = 0 # count units of sand
  sand = set() # positions where sand is rested
  max_y = max(y for _, y in rocks) # if sand goes pass that --> abyss!
  abyss = False

  while not abyss:
    sand_src = (500, 0)
    sand_pos = sand_src
    rest = False
    
    while not rest:
      for move in ((0,1), (-1,1), (1,1)):
        next_pos = sand_pos[0] + move[0], sand_pos[1] + move[1]
        if next_pos not in rocks | sand:
          moved = True # next cell is air, can move
          sand_pos = next_pos # move sand
          break
        # no available next move
        moved = False # all next cells are either rocks or sand, can't move --> must rest

      if sand_pos[1] > max_y:
        abyss = True
        break
      if moved == False:
        rest = True
        sand.add(sand_pos)
        count += 1

  return count

print("part1:", part1())
