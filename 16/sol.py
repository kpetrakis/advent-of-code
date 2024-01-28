#!/usr/bin/env python3
import re
from functools import cache
from collections import defaultdict
import itertools
from math import inf as INF

r = r'(\b[A-Z]{2}) .*=(\d*); .* valves? (.*)'
V = set()
F = dict()
D = defaultdict(lambda: INF) # distance dict
with open('input.txt', 'r') as f:
  for v, rate, neighbors in re.findall(r, f.read()):
    V.add(v)
    if rate != '0': # without that check it recursed for a very long time
      F[v] = int(rate)
    for u in neighbors.split(', '):
      D[v,u] = 1

# floyd-warshall
for k, i, j in itertools.product(V, V, V):
  D[i, j] = min(D[i, j], D[i, k] + D[k, j])

@cache
def search(t, v, unopened, e=False):
  if t <= 0:
    return 0

  # max_pressure = 0
  # for u in unopened:
  #   max_pressure = max(max_pressure, F[u] * (t - D[v,u] - 1) + search(t-D[v,u]-1, u, unopened-{u}))

  # the above loop in one line
  max_pressure = max(itertools.chain([search(26, 'AA', unopened) if e else 0], (F[u] * (t-D[v,u]-1) + search(t-D[v,u]-1, u, unopened-{u}, e) for u in unopened)))

  return max_pressure

max_pressure = search(30, 'AA', frozenset(F)) # stin arxi oles einai unopened, frozenset gia na einai hashable
print("Part 1:", max_pressure)
max_pressure2 = search(26, 'AA', frozenset(F), e=True)
print("Part 2:", max_pressure2)

