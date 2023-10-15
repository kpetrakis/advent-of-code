#!/usr/bin/env python

def parse_input(filename):
  sensors = []
  beacons = []
  with open(filename, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
      line_elements = line.split(' ')
      sensor = int(line_elements[2].strip(',').split('=')[1]), int(line_elements[3].strip(':').split('=')[1]) # x,y
      beacon = int(line_elements[-2].strip(',').split('=')[1]), int(line_elements[-1].strip().split('=')[1])
      sensors.append(sensor)
      beacons.append(beacon)

    return sensors, beacons


def manhattan_distance(p1, p2):
  x1, y1 = p1
  x2, y2 = p2 
  return abs(x1-x2) + abs(y1-y2) 

sensors, beacons = parse_input('input.txt')

def part1():
  y = 2000000
  positions = set() # valid positions for a beacon on the given y row
  for s, b in zip(sensors, beacons):
    max_dist = manhattan_distance(s, b) # max distance if s and b where collieear
    sx, sy = s
    if abs(sy-y) < max_dist: # if y row within s radius (max_dist)
      x_dist = max_dist - abs(sy-y) # the distance in x-axis from s to b
      for x in range(sx-x_dist, sx+x_dist+1):
        positions.add((x,y))

  positions = positions - set(beacons) # don't count the B points
  return len(positions)

print("part1:", part1())
