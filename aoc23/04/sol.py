#!/usr/bin/env python
import re
from collections import defaultdict

def parse(file: str) -> list :
  with open(file, "r") as f:
    data = f.read().split('\n')
  return data

data = parse("input.txt")
# print(f" data : {data}")

def part1() -> int:
  SUM = 0
  for line in data:
    left, right = line.split("|")
    winning_numbers = set(int(x) for x in re.findall(r"\d+", left.split(":")[1]))
    have_numbers = set(int(x) for x in re.findall(r"\d+", right))
    # print(f"set &: {winning_numbers & have_numbers}")
    # print(f"set &: {winning_numbers.intersection(have_numbers)}")
    if (common_numbers:= winning_numbers & have_numbers):
      SUM += 2**(len(common_numbers)-1)
    else:
      pass
  return SUM
  
def part2() -> int:
  copies = defaultdict(lambda: 1)
  CARD_NUMBERS = set() # used to add all the copies[card_number] that have not been populated and have value 1
  for i, line in enumerate(data):
    left, right = line.split("|")
    card_number = int(re.findall(r"\d+", left.split(":")[0]).pop())
    CARD_NUMBERS.add(card_number)
    winning_numbers = set(int(x) for x in re.findall(r"\d+", left.split(":")[1]))
    have_numbers = set(int(x) for x in re.findall(r"\d+", right))
    if (common_numbers:= winning_numbers.intersection(have_numbers)):
      num_copies = len(common_numbers)
      # print("num copies:", num_copies)
      # print(f"copies[{card_number}] = {copies[card_number]}")
      for i in range(card_number+1, card_number+1+num_copies):
        copies[i] += 1 * copies[card_number]

  SUM = sum(copies[n] for n in CARD_NUMBERS)
  return SUM

print(f"Part 1: {part1()}")
print(f"Part 2:", part2())