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


def find_empty_space(l):
  '''
  l: [(start, end), (start, end), ...] sorted on start
  '''
  cmp = l[0] # the first (start, end) in l
  for i in range(1, len(l)):
    start, end = l[i]
    if start >= cmp[0] and end <= cmp[1]:
      continue
     
    if start - cmp[1] > 1:
      # found the empty space
      return start-1
    cmp = (start, end)
  return -1

def part2():
  for y in range(4000000):
    intervals_set = set() # set containing {(start,end), (start,end),..} for each line
    for s, b in zip(sensors, beacons):
      max_dist = manhattan_distance(s, b) # max distance if s and b where collieear
      sx, sy = s
      if abs(sy-y) < max_dist: # if y row within s radius (max_dist)
        x_dist = max_dist - abs(sy-y) # the distance in x-axis from s to b
        interval = (sx-x_dist, sx+x_dist) # interval : (start, end) in row y 
        intervals_set.add(interval)
    # sort based on start
    list_of_start_end_pairs = sorted(intervals_set) # sorted turns set --> list
    x = find_empty_space(list_of_start_end_pairs)
    if x != -1:
      #print("found:", (x,y))
      #print("answer:", 4000000*x + y)
      return 4000000*x + y

print("part1:", part1())
print("part2:", part2())
