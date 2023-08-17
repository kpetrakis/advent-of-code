#!/usr/bin/env python3
"""
A: rock
B: paper
C: scissor

strategy --> score
X: i need to loose 
Y: i need to draw 
Z: i need to win 

C > B > A > C 
"""

from itertools import pairwise, cycle, product
data = open("input.txt", "r").read().split('\n')

# print(data)

hands = ['A', 'B', 'C']
# mappings = {'X':'A', 'Y':'B', 'Z':'C'}
shape_score = {'A':1, 'B':2, 'C':3}

def find_move(opponent_hand, outcome):
  assert outcome in ['X', 'Y', 'Z']

  index = hands.index(opponent_hand)

  if outcome == 'Y':
    # draw
    return hands[index] # the same hand as the opponent
  elif outcome == 'X':
    # loose 
    if index == 0:
      return hands[len(hands) - 1] # the previous of the first hand is the last hand
    else:
      return hands[index - 1] # play the previous hand from the opponent
  elif outcome == 'Z':
    # win
    if index == len(hands) - 1:
      return hands[0]
    else:
      return hands[index + 1] # play the next hand from the opponent

print("All possible results:", list(product(hands, hands, repeat=1)))

winning_hands = set() # winner on the second column!
print("Winning hands when i am the player in the second column :")
for i, hand in enumerate(pairwise(cycle(hands))):
  if i == 3:
    break
  # print(item)
  winning_hands.add(hand)

print(winning_hands)

total_score = 0
for d in data:
  # ignore emtpy lines
  if d.strip():
    pair = d.split(' ') # e.g ['A', 'Y']
    pair = tuple(pair)
    # print(pair)
    move = find_move(pair[0], pair[1])
    # print(move)
    game_pair = (pair[0], move)
    # print(game_pair)
    if game_pair in winning_hands:
      # win
      score = shape_score[game_pair[1]] + 6
    elif game_pair[0] == game_pair[1]:
      # draw
      score = shape_score[game_pair[1]] + 3
    else:
      # lost
      score = shape_score[game_pair[1]]

    total_score += score

print("Total score:", total_score)
