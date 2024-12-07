#!/usr/bin/env python3
from part1 import create_letters_list

data = open("input.txt", "r").readlines()
# this parsing is terrible!
data = [[data[i].strip(), data[i+1].strip(),data[i+2].strip()] for i in range(0, len(data), 3)]
# print("data", data)

letters = create_letters_list() 
priorities_sum = 0
for group in data:
  # print("group:", group)
  group_sacks = []
  for sack in group:
    items_in_sack = set(sack) # the unique items in a sack (no duplicates)
    group_sacks.append(items_in_sack)
    # print("items in sack:", items_in_sack)

  # print("group sacks:", group_sacks)
  d1, d2, d3 = group_sacks
  # common_item = d1 & d2 & d3
  common_item = d1.intersection(d2, d3).pop()
  # print("common item", common_item)
  priority = letters.index(common_item) + 1
  priorities_sum += priority


print("priorities sum:", priorities_sum)
