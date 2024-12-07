#!/usr/bin/env python3
from collections import deque
data = open("ex.txt", "r").readlines()#.read().split('\n\n')
print("data:", data)

def filter_row(row):
  """
  filtrarei ena row
  """
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

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13
# 0 4 8 12 16 20
# 0 1 2 3  4  5

moves = [] # a list holding the coding of moves
stack_numbers = [] # oi arithmoi twn stacks
for d in data:
  d = d.strip('\n')
  row = d.split(' ') # ['', '','','','[D]','','','','','']
  print("row:", row)
  if len(row) ==1 or len(row) > 1 and row[1] == '1':
    continue
  row = filter_row(row)
  print(row)
  # indexes_of_letters = [i for i, item in enumerate(row) if item]
  # print(indexes_of_letters)
  # print([index // 4 for index in indexes_of_letters])
  # while row.__contains__(''):
  #   row.remove('')
  # row = list(filter(None, row))
  # print("after row:", row)

  if len(row) > 1 and row[0] == '' and row[1] == '1':
    number_of_stacks = max([int(item) if item else 0 for item in row])

print(number_of_stacks)
