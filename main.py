from timeit import timeit
formatted = []

# c - cookies, b - bamboo, t - wan, e,s,w,n,z,f,g
# g- baiban
# sequence should be 14 length
# each set should have 3 elements
# 4 sets + 1 pair
# lookup defines a: ascending set, i: identical set

HAND_THIRTEEN_ORPHANS = [
    'b1', 'b9',      # bamboo 1 and 9
    'c1', 'c9',      # circles 1 and 9
    't1', 't9',      # characters 1 and 9
    'e', 's', 'w', 'n',  # four winds
    'z', 'f', 'g',   # three dragons# duplicate (any one of the 13, here bamboo 1)
]

HAND_THIRTEEN_ORPHANS.sort()

def thirteen_match(on: int = 0, character: chr = "", offset: int = 0):
  if HAND_THIRTEEN_ORPHANS[on - 1 + offset] == character:
    if HAND_THIRTEEN_ORPHANS[on - 2 + offset] == character:
      return 0, 0
    return 1, -1
  elif HAND_THIRTEEN_ORPHANS[on + offset] == character: # find a way to swap it around cause this happens more
    return 1, 0 
  return 0, 0
class Set:
  now: int
  s: tuple[str, str, str, str, str, str, str, str, str]
  def __init__(self):
    self.now = 0
    self.s = [""] * 9
  def add (self, a):
    self.s[self.now] = a
    self.now += 1

def normal_match(a: chr = "", sets: list[Set, Set, Set, Set, Set, Set, Set] = [Set(), Set(), Set(), Set(), Set(), Set(), Set()]):
  for set in sets:
    # if set.now == 4: # dont need can see how big the set can go
      # continue
    if set.now == 0:
      set.add(a)  
      return 1, sets
    match a[0]:
      case "c" | "b" | "t":
        seek = a[0] + str(int(a[1]) - 1) # might store seek at the first element of each list
        if set.s[set.now - 1] == seek:
          set.add(a)
          return 1, sets
    if set.s[0] == a: #check same 
      set.add(a)
      return 1, sets
    if set.now == 1:
      return 0, None


def match(hand):
  a = 1 # thirteen
  b = 1 #normal
  sets = [Set(), Set(), Set(), Set(), Set(), Set(), Set()]
  offset = 0 
  for i, t in enumerate(hand):
    if a != 0:
      a, o = thirteen_match(i,t, offset)
      offset += o
    if b != 0:
      b, sets = normal_match(t, sets)

  return a, b , sets

def matcher():
  return 0
# Collection of valid Mahjong winning hands
WINNING_HANDS = {
    "mixed_1": [
        'b2', 'b3', 'b4',   # bamboo 2-3-4
        'c7', 'c7', 'c7',   # circles 7 triplet
        't5', 't6', 't7',   # characters 5-6-7
        'e', 'e', 'e',      # east wind triplet
        'n', 'n'            # north wind pair
    ],
    "all_chows": [
        'b1', 'b2', 'b3',
        'b4', 'b5', 'b6',
        'c2', 'c3', 'c4',
        't7', 't8', 't9',
        'c8', 'c8'
    ],
    "all_pungs": [
        'b3', 'b3', 'b3',
        'c8', 'c8', 'c8',
        't1', 't1', 't1',
        'z', 'z', 'z',
        's', 's'
    ],
    "all_honors": [
        'e', 'e', 'e',
        's', 's', 's',
        'w', 'w', 'w',
        'z', 'z', 'z',
        'f', 'f'
    ],
    "terminals_and_honors": [
        'b1', 'b2', 'b3',
        'b9', 'b9', 'b9',
        'c1', 'c1', 'c1',
        't9', 't9', 't9',
        'n', 'n'
    ],
    "three_dragons": [
        'z', 'z', 'z',
        'f', 'f', 'f',
        'g', 'g', 'g',
        'b5', 'b6', 'b7',
        'c2', 'c2'
    ],
    "bamboo_flush": [
        'b1', 'b2', 'b3',
        'b4', 'b5', 'b6',
        'b7', 'b8', 'b9',
        'b2', 'b2', 'b2',
        'b5', 'b5'
    ],
    "outside_hand": [
        'b1', 'b2', 'b3',
        'b9', 'b9', 'b9',
        'c1', 'c2', 'c3',
        'e', 'e', 'e',
        's', 's'
    ],
    "all_simples": [
        'b2', 'b3', 'b4',
        'b5', 'b6', 'b7',
        'c3', 'c4', 'c5',
        'c6', 'c7', 'c8',
        't4', 't4'
    ],
    "thirteen_orphans": [
        'b1', 'b9', 'c1', 'c9', 't1', 't9',
        'e', 's', 'w', 'n', 'z', 'f', 'g',
        'b1'  # duplicate
    ],
    "thirteen_orphans_v2": [
        'b1', 'b9', 'c1', 'c9', 't1', 't9',
        'e', 's', 'w', 'n', 'z', 'f', 'g',
        'z'   # duplicate red dragon
    ]
}

# Example: Access a hand
def benchmark():
  for key, value in WINNING_HANDS.items():
    print(key)
    value.sort()
    a, b, sets = match(value)
    print(a, b)
    if b == 1:
      for set in sets:
        print(set.s)

t = timeit(benchmark, number=100)
print(f"done in {t}")