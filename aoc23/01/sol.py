#!/usr/bin/env python3
import re

r = r"\d"
r2 = r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))"

def parse(file: str) -> list[str]:
  with open(file, 'r') as f:
    data = f.read().split("\n")
    return data

word_to_digit = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
data = parse('input.txt')
calib_sum = 0
reg = re.compile(r2)
for s in data:
  # print(s, reg.findall(s))
  # calib = int(reg.findall(s)[0] + reg.findall(s)[-1])
  calib_numbers = list(map(lambda x: word_to_digit[x] if x.isalpha() else x, reg.findall(s)))
  print(s, calib_numbers)
  calib_sum += int(calib_numbers[0] + calib_numbers[-1])

#print("Part 1: ", calib_sum)
print("Part 2: ", calib_sum)

