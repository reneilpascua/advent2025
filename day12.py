from typing import Optional, TextIO, List, Tuple

# choose the appropriate return for the input
def process_input(f: TextIO) -> Tuple[List,List,List]: 
    raw = f.readlines()
    shapes, dimensions, ngifts = [],[],[]

    # there are 6 shapes
    for i in range(6):
      shapes.append([row.strip() for row in raw[ 5*i+1 : 5*i+4]])

    # dimensions and ngifts start at i=30
    for row in raw[30:]:
        row_ = row.split(': ')
        dimensions.append([int(c) for c in row_[0].split('x')])
        ngifts.append([int(c) for c in row_[1].split(' ')])

    return shapes, dimensions, ngifts
    
def solve1(shapes, dimensions, ngifts):
  pass

def solve2(shapes, dimensions, ngifts):
  pass

def main(example: Optional[Tuple[List,List,List]] = None):
  with open('./day12_input.txt') as f:
    shapes, dimensions, ngifts = process_input(f) \
      if not example else example
    solve1(shapes, dimensions, ngifts)
        

if __name__ == '__main__':
  example = (
    [[
    "###",
    "##.",
    "##.",
    ],
    [
    "###",
    "##.",
    ".##",
    ],
    [
    ".##",
    "###",
    "##.",
    ],
    [
    "##.",
    "###",
    "##.",
    ],
    [
    "###",
    "#..",
    "###",
    ],
    [
    "###",
    ".#.",
    "###",
    ]],
    [[4,4],[12,5],[12,5]],
    [[0, 0, 0, 0, 2, 0],[1, 0, 1, 0, 2, 2],[1, 0, 1, 0, 3, 2]]
  )
  main(example)
  # main()