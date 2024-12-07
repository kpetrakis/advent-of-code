#!/usr/bin/env python3
import re

r = r"\d"

def parse(file: str) -> list[str]:
  with open(file, 'r') as f:
    data = f.read().split("\n")
    return data

data = parse('input.txt')
calib_sum = 0
reg = re.compile(r)
for s in data:
  # print(s, reg.findall(s))
  calib = int(reg.findall(s)[0] + reg.findall(s)[-1])
  calib_sum += calib

print("Part 1: ", calib_sum)

