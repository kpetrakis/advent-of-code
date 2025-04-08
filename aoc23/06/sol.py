#!/usr/bin/env python
import re
import operator
from functools import reduce 
from itertools import starmap

def parse(file: str) -> list:
  with open(file, 'r') as f:
    row1, row2 = f.read().split("\n")
    times = map(int, re.findall(r'(\d+)', row1))
    distances = map(int, re.findall(r'(\d+)', row2))

  return list(times), list(distances)

times, distances = parse("input.txt")

def part1():
  total = 1
  for time, dist in zip(times, distances):
    num_ways = 0
    for hold in range(0, time+1):
      speed = hold
      milimiters = (time - hold) * speed

      if milimiters > dist:
        num_ways += 1

    total *= num_ways

  return total

time = int(''.join(map(str, times)))
dist = int(''.join(map(str, distances)))

def part2():
  total = 1
  pairs = zip(range(time), range(time, 0, -1))
  # products = [reduce(operator.mul, pair) for pair in pairs]
  num_ways = sum(1 for x in filter(lambda x: x>dist, starmap(operator.mul, pairs)))
  total *= num_ways

  return total

print("Part1 = ", part1())
print("Part2 = ", part2())