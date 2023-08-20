#!/usr/bin/env python3

data = open("input.txt", "r").read().split('\n')
# print(data)

def create_letters_list():
  """
  create a list with all the letters
  note: i could use string.ascii_letters and it would be EASIER!!!
  but i did it the hard (dumm??) way ;)
  """
  letters = list()
  for l in range(ord('a'), 0x7B): # ord('a'), ord('z') inclusive
    letters.append(chr(l))

  for l in range(ord('A'), 0x5B):
    letters.append(chr(l))

  # for i, l in enumerate(letters):
  #   print(i+1, l)

  return letters

if __name__ == "__main__": # because of the import in part2 
  letters = create_letters_list() 
  priorities_sum = 0
  for d in data:
    # ignore empty lines
    if d.strip():
      first_comp = set(d[:len(d)//2])
      second_comp = set(d[len(d)//2:])
      # print(first_comp, second_comp)

      # find the item type that appears in both compartments
      for item in first_comp:
        if item in second_comp:
          same_item = item
          # print("same item:", item)

      priority = letters.index(same_item) + 1
      priorities_sum += priority
      # print(priority)

  print("sadf", priorities_sum)
