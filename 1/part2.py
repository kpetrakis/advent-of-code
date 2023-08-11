#!/usr/bin/env python3
data = open("input.txt", "r").read().split("\n\n")

calories_per_elf = []
for elf, calories in enumerate(data):
  calorie_sum = sum([int(c) if c else 0 for c in calories.split('\n')])
  calories_per_elf.append(calorie_sum)

top3_calories = sorted(calories_per_elf, reverse=True)[:3]
top3_calories_sum = sum(sorted(calories_per_elf, reverse=True)[:3])
print("Top 3 elfs calories sum:", top3_calories_sum)

