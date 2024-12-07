#!/usr/bin/env python
from functools import cmp_to_key

def parse(filename):
  with open(filename, 'r') as f:
    lines =  [line.strip() for line in f.readlines()]
    return lines

def compare(packet1, packet2):
  """
  class patterns are cool!
  """
  #print("comparing:", packet1, packet2)
  match packet1, packet2:
    case int(), int():
      if packet1 < packet2:
        return 1
      elif packet1 > packet2:
        return -1
      else:
        return 0
    case list(), list():
      for v in map(compare, packet1, packet2):
        if v: # if v not 0 continue with next element
          return v
      # ola ta items twn lists itan isa. check if packet1 run out of items first
      return compare(len(packet1), len(packet2))
    case list(), int():
      return compare(packet1, [packet2])
    case int(), list():
      return compare([packet1], packet2)


def part1():
  lines = parse('input.txt')
  orders = list()
  index = 1
  sum_of_indexes = 0
  for i in range(0, len(lines), 3): # 2
    packet1 = eval(lines[i])
    packet2 = eval(lines[i+1])
    order = compare(packet1, packet2)
    if order == 1:
      sum_of_indexes += index
    index += 1
  return sum_of_indexes

def part2():
  divider1, divider2 = [[2]], [[6]]
  packets = []
  lines = parse('input.txt')
  for i in range(0, len(lines), 3): # 2
    packet1 = eval(lines[i])
    packet2 = eval(lines[i+1])

    packets.append(packet1)
    packets.append(packet2)

  packets.extend([divider1, divider2])
  packets.sort(key=cmp_to_key(compare), reverse=True) # check sorting HOWTO

  index1 = packets.index(divider1) + 1
  index2 = packets.index(divider2) + 1
  decoder_key = index1 * index2
  return decoder_key
    

answer1 = part1()
print("part1:", answer1)

answer2 = part2()
print("part2:", answer2)
