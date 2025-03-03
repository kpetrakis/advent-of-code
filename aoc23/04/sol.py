#!/usr/bin/env python
import re

def parse(file: str) -> list :
  with open(file, "r") as f:
    data = f.read().split('\n')
  return data

data = parse("input.txt")
# print(f" data : {data}")

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
  
print(f"Part 1: {SUM}")