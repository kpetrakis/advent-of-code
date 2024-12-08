#!/usr/bin/env python

"""
each cube has 6 sides.
1 side immediately connected -> 5 open
"""

def parse(file: str) -> list:
  with open(file, 'r') as f:
    data = f.read().split("\n")
    coords = list()
    for s in data:
      coords.append(tuple(map(int, s.split(','))))
  return coords

cubes = parse('input.txt')

sum_of_exposed_sides = 0
# use itertools permutations or something?
for i in range(len(cubes)):
  sides_exposed = {'x_right':True, 'x_left':True, 'y_front':True, 'y_back':True, 'z_up':True, 'z_down':True} 
  cube = cubes[i] # cube for which I count free sides
  for c in cubes[:i] + cubes[i+1:]: # compare with all the others
    if cube[0] == c[0] - 1 and cube[1] == c[1] and cube[2] == c[2]:
      sides_exposed['x_right'] = False
    if cube[0] == c[0] + 1 and cube[1] == c[1] and cube[2] == c[2]:
      sides_exposed['x_left'] = False
    if cube[1] == c[1] - 1 and cube[0] == c[0] and cube[2] == c[2]:
      sides_exposed['y_back'] = False
    if cube[1] == c[1] + 1 and cube[0] == c[0] and cube[2] == c[2]:
      sides_exposed['y_front'] = False
    if cube[2] == c[2] - 1 and cube[0] == c[0] and cube[1] == c[1]:
      sides_exposed['z_up'] = False
    if cube[2] == c[2] + 1 and cube[0] == c[0] and cube[1] == c[1]:
      sides_exposed['z_down'] = False
  #print(sides_covered)
  #print(cube, sides_exposed.values(), sum(sides_exposed.values()))
  #print(i, (sum(sides_exposed.values())))
  sum_of_exposed_sides += sum(sides_exposed.values())

# Part 1: 4320
print("part 1:", sum_of_exposed_sides)
