#!/usr/bin/env python3

data = open("input.txt", "r").readlines()#.read().split('\n\n')

# SOS otan exw range(x,x) tote prokiptei empty set kai i sinthiki pou exw tha isxei enw den prepei! -> range(x,x+1)!
count = 0
for d in data:
  pair = d.strip('\n').split(',') # ['2-4', '6-8']
  print(pair)
  elf1_sections, elf2_sections = pair[0], pair[1] # 2-4, 6-8
  # section range for 1st elf
  elf1_start, elf1_end = elf1_sections.split('-')
  elf1_start, elf1_end = int(elf1_start), int(elf1_end) 
  elf1_range = range(elf1_start, elf1_end + 1) # range is not inclusive!
  print("elf1 range", elf1_range)
  # section range for 2nd elf
  elf2_start, elf2_end = elf2_sections.split('-')
  elf2_start, elf2_end = int(elf2_start), int(elf2_end) 
  elf2_range = range(elf2_start, elf2_end + 1)
  print("elf2 range", elf2_range)

  if (set(elf1_range) & set(elf2_range)):
    # if the intersection has at least one item then they overlap
    count += 1

print("Count:", count)
