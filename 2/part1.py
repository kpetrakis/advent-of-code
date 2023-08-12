#!/usr/bin/env python3
"""
A: rock
B: paper
C: scissor

strategy --> score
X: rock --> 1
Y: paper --> 2
Z: scissor --> 3

winninigs
A > C | C > B | B > A
or
A > Z | C > Y | B > X

or more concretely:
C > B > A > C 
Idea: i need cyclic list to define the winner
"""

from itertools import pairwise, cycle, product
data = open("ex.txt", "r").read().split('\n')

# print(data)

hands = ['A', 'B', 'C']
mappings = {'X':'A', 'Y':'B', 'Z':'C'}
shape_score = {'A':1, 'B':2, 'C':3}

print("All possible results:", list(product(hands, hands, repeat=1)))

winning_hands = set() # winner on the second column!
print("Winning hands when i am the player in the second column :")
for i, item in enumerate(pairwise(cycle(hands))):
  if i == 3:
    break
  # print(item)
  winning_hands.add(item)

print(winning_hands)

total_score = 0
for d in data:
  # ignore emtpy lines
  if d.strip():
    pair = d.split(' ') # e.g ['A', 'Y']
    pair[1] = mappings[pair[1]] # replace X, Y, Z with A, B, C
    pair = tuple(pair)
    if pair in winning_hands:
      # win
      score = shape_score[pair[1]] + 6
    elif pair[0] == pair[1]:
      # tie
      score = shape_score[pair[1]] + 3
    else:
      # lost
      score = shape_score[pair[1]]

    # print(f"pair: {pair} | score: {score}")
    total_score += score

print("Total score:", total_score)
