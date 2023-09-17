#!/usr/bin/env python
import math
from collections import deque
from functools import reduce

class Monkey:
  def __init__(self, monkid, items, operation, divisible_by,  monktrue, monkfalse):
    self.monkid = monkid
    self.items = deque() 
    self.operation = operation
    self.divisible_by = divisible_by
    self.monkey_true = monktrue
    self.monkey_false = monkfalse 
    for item in items:
      self.items.append(item)
    self.COUNT = 0
  
  def inspect(self):
    throwings = list() # list [(worry_level, monkey_idx), ...]
    for item in list(self.items)[:]: # in place copy!
      worry_level = self.exec_operation(item)
      # print(worry_level)
      self.COUNT += 1
      if worry_level % self.divisible_by == 0:
        # throw to monkey_true
        throwings.append((worry_level, self.monkey_true))
      else:
        # throw to monkey_false
        throwings.append((worry_level, self.monkey_false))
      self.items.popleft() # pop the item i just checked

    return throwings

  def exec_operation(self, item):
    old = item
    return eval(self.operation) // 3

  def receive_item(self, worry_level):
    """
    used to add items thrown by another monkey in the items deque
    """
    self.items.append(worry_level)


data = open('input.txt', 'r').read().strip().split('\n')
# print(data)

monkeys = list() # all the monkeys 
for i in range(0, len(data), 7):
  monkey_id = int(data[i].split(' ')[1].strip(':')) 
  # print(monkey_id)
  items = [int(item.strip(',')) for item in data[i+1].split(' ')[4:]]
  # print(items)
  operation = ' '.join(data[i+2].strip(' ').split(' ')[3:])
  # print(operation)
  divisible_by = int(data[i+3].strip(' ').split(' ')[-1]) # test operator
  # print(divisible_by)
  monkey_if_true = int(data[i+4].strip(' ').split(' ')[-1])
  # print('monkey true:', monkey_if_true)
  monkey_if_false = int(data[i+5].strip(' ').split(' ')[-1])
  # print('monkey true:', monkey_if_false)

  monkey = Monkey(monkey_id, items, operation, divisible_by, monkey_if_true, monkey_if_false)
  monkeys.append(monkey)

def round():
  for monkey in monkeys:
    throwings = monkey.inspect() # index of the monkey to throw item
    # print(throwings)
    for worry_level, monkidx in throwings:
      monkeys[monkidx].receive_item(worry_level)

# run 20 rounds
for r in range(1, 21):
  round()
  # print("round", r)
  # for i, monkey in enumerate(monkeys):
  #   print(i, monkey.items, monkey.COUNT)
  # print("----------------------------")

# after 20 rounds
counts = []
for i, monkey in enumerate(monkeys):
  counts.append(monkey.COUNT)
print("answer part 1:", reduce(lambda x, y: x*y, sorted(counts, reverse=True)[:2]))


