#!/usr/bin/env python3
from collections import deque
data = open("input.txt", "r").readlines()#.read().split('\n\n')

def filter_row(row):
  l = list()
  i = 0
  while i < len(row):
    if row[i] == '' and row[i+1] == '' and row[i+2]=='':
      l.append('')
      i += 4
    else:
      l.append(row[i])
      i += 1
  return l

def print_stacks(stacks):
  for i, stack in enumerate(stacks):
    print(i, stack)

# find the number of stacks
for d in data:
  d = d.strip('\n')
  row = d.split(' ') # ['','','','[D]','','','','','']
  if len(row) > 1 and row[0] == '' and row[1] == '1':
    number_of_stacks = max([int(item) if item else 0 for item in row])
# print("number of stacks:", number_of_stacks)

stacks = [deque() for _ in range(number_of_stacks)]
moves = [] # a list holding the coding of moves
for d in data:
  d = d.strip('\n')
  row = d.split(' ') # ['', '','','','[D]','','','','','']
  # parsing the moves
  if row[0] == "move":
    count, src, dst = int(row[1]), int(row[3]), int(row[5])
    moves.append((count, src-1, dst-1)) # adapt to zero based indexing
    continue
  
  # print("row:", row)
  # only filter letter rows
  if len(row) == 1 or len(row) > 1 and row[1] == '1':
    continue
  row = filter_row(row)
  # print("filtered row:", row)

  # populating the stacks
  for i, item in enumerate(row):
    if item: # and den einai empty ''
      stacks[i].appendleft(item.strip('[').strip(']'))

print("Initial stacks:")
print_stacks(stacks)

# make the moves
for move in moves:
  count, src, dst = move
  for _ in range(count):
    item = stacks[src].pop()
    stacks[dst].append(item)

print("Result stacks:")
print_stacks(stacks)
topofstacks = []
for stack in stacks:
  top = stack.pop()
  topofstacks.append(top)

answer = ''.join(topofstacks)
print("answer:", answer)
