#!/usr/bin/env python
from collections import deque
from itertools import islice

data = open("input.txt", 'r').readlines()
data = [d.strip('\n') for d in data]
# print(len(data))

cycles_of_interest = [20, 60, 100, 140, 180, 220]

values = deque() # to expand operand values in the cycle number that will be added to X
for command in data:
  if command == 'noop':
    values.append(0)
  else:
    opcode, operand = command.split(' ')
    assert opcode == 'addx'
    values.append(0)
    values.append(int(operand))

# print(values)
X = 1 # register
values.appendleft(X) # prosthetw tin arxiki timi tou X - kanei swsti tin arithmisi twn cycles
# print(deque(islice(l, 0, 20)))
answer1 = sum((sum(islice(values, 0, cycle)) * cycle for cycle in cycles_of_interest))
print("answer part 1:", answer1)

# part2
print("answer part 2:") # answer = EJCFPGLH
width, height = 40, 6
sprite_pos = sum(islice(values, 0, 1)) # initial sprite pos
for i in range(height):
  line = []
  for j in range(width):
    cycle = i*width + (j+1) #(i + 1) * (j + 1)
    if sprite_pos - 1 <= j <= sprite_pos + 1:
      line.append('#');
    else:
      line.append('.')
    sprite_pos = sum(islice(values, 0, cycle + 1))
    # # print(list(islice(values, 0, cycle)))
    #print("cycle:", cycle)
    #print("sprite position:", sprite_pos)
    #print(''.join(line))
  print(''.join(line)) # new line
