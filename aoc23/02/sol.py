#!/usr/bin/env python
import re

#r = r"\bGame (\d+):\s*(\d+\s*(?:blue|red|green)(?:,\s*))"
#r = r"\bGame (\d+): (\d+ (?:blue|red|green),?)"
#r = r"Game (\d+):.*(\d+)"
r1 = r"Game (\d+)"
r2 = r";\s*"

def parse(file: str) -> list :
  with open(file, 'r') as f:
    data = f.read().split('\n')
    return data

data = parse('input.txt')
def part1():
  id_sum = 0
  for sen in data:
    game_id = re.findall(r1, sen)[0]
    #print(game_id)
    cube_subsets = re.split(r2, sen.split("Game "+game_id+": ")[1])
    #print(cube_subsets)
    is_subset_possible = [False] * len(cube_subsets)
    #print(is_subset_possible)
    for i, subset in enumerate(cube_subsets):
      #cnt, color = subset.split(", ")
      color_cnt_strs = subset.split(", ")
      d = {'red':0, 'blue':0, 'green':0}
      #print("before", d)
      for color_cnt in color_cnt_strs:
        cnt, color = color_cnt.split(" ")
        d[color] = int(cnt)
      #print("after", d)
      if d['red'] <= 12 and d['green'] <= 13 and d['blue'] <= 14:
        is_subset_possible[i] = True
        #print("possible subset :", i)

    if all(is_subset_possible):
      id_sum += int(game_id)
      #print("possible game with ID:", game_id)
  
  return id_sum

print("part 1:", part1())

