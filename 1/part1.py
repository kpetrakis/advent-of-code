#!/usr/bin/env python3
data = open("input.txt", "r").read().split("\n\n")

max_calories = sum([int(c) if c else 0 for c in data[0].split('\n')])
max_elf = 0
for elf, calories in enumerate(data[1:], start=1):
  calorie_sum = sum([int(c) if c else 0 for c in calories.split('\n')])
  # print(elf, calorie_sum)
  if calorie_sum > max_calories:
    max_calories = calorie_sum 
    max_elf = elf

print(f"Max elf:{max_elf}, max calories: {max_calories}")
