from typing import Optional, Tuple, List

def get_area(p1: List[int], p2: List[int]) -> int:
  x, y = abs(p2[0]-p1[0])+1, abs(p2[1]-p1[1])+1
  return x*y

def main1(example: Optional[List[List[int]]] = None):
  with open('./day09_input.txt') as f:
    input = [[int(d) for d in line.split(',')] for line in f.readlines()] if not example else example

    # naive soln: compare all points to each other O(n^2)
    n = len(input)
    largest = 0
    for i in range(n):
      for j in range(i+1,n):
        largest = max(largest, get_area(input[i], input[j]))
    print(largest)

    # according to chatgpt, u would use "convex hull" for this...
    # which isn't really leetcode/interview friendly

def main2(example: Optional[List[List[int]]] = None):
  with open('./day09_input.txt') as f:
    input = [[int(d) for d in line.split(',')] for line in f.readlines()] if not example else example
    n = len(input)

    # CONVENTION:
    # coordinates go (x,y)
    # x = left right = column; y = up down = row

    # BOUNDARIES ###########################################################

    # bound the space
    xi, yi = input[0]
    xf, yf = input[0] # just to init
    for point in input[1:]:
      xi = min(xi, point[0])
      xf = max(xf, point[0])
      yi = min(yi, point[1])
      yf = max(yf, point[1])
    # now the square of (xi,yi) to (xf,yf) contains all the points

    # DRAW THE BOUNDARIES ##################################################
    print(f'{xi=} {xf=} size = {xf-xi}')
    print(f'{yi=} {yf=} size = {yf-yi}')

    # for row y = Y, what is the leftest and rightest x could be?
    xbounds: List[List] = [[float('inf'), float('-inf')] for _ in range(yf-yi+1)]
    # for col x = X, what is the lowest and highest y could be?
    ybounds: List[List] = [[float('inf'), float('-inf')] for _ in range(xf-xi+1)]
    
    def drawbounds(t1, t2, s, same_is_x):
      si, ti = (xi, yi) if same_is_x else (yi, xi)
      sbounds = xbounds if same_is_x else ybounds
      for j in range(t1-ti, t2-ti+1):
        sbj = sbounds[j]
        sbj[0] = min(sbj[0], s)
        sbj[1] = max(sbj[1], s)
      tbs = ybounds[s-si] if same_is_x else xbounds[s-si]
      tbs[0] = min(tbs[0], t1)
      tbs[1] = max(tbs[1], t2)


    # draw the boundaries
    for i in range(n): # trick: make sure to connect the first to the last as well
      p1, p2 = input[i-1], input[i]
      x1, x2 = (p1[0], p2[0]) if p1[0]<p2[0] else (p2[0], p1[0])
      y1, y2 = (p1[1], p2[1]) if p1[1]<p2[1] else (p2[1], p1[1])
      if y1==y2:
        drawbounds(x1, x2, y1, same_is_x=False)
      elif x1==x2:
        drawbounds(y1, y2, x1, same_is_x=True)
      else: raise Exception('the 2 points must be on the same x or y line!')
    print('finished drawing!')

    # HELPER FUNCTIONS TO DETERMINE INBOUNDS ###############################
    def get_max_min(l: List[List]) -> List:
      max_minbound = l[0][0]
      min_maxbound = l[0][1]
      for sub in l[1:]:
        max_minbound = max(max_minbound, sub[0])
        min_maxbound = min(min_maxbound, sub[1])
      return [max_minbound, min_maxbound]

    def get_xbounds(y1: int, y2: int) -> List:
      nonlocal yi, xbounds
      subxbounds = xbounds[y1-yi : y2-yi+1]
      return get_max_min(subxbounds)
    
    def get_ybounds(x1: int, x2: int) -> List:
      nonlocal xi, ybounds
      subybounds = ybounds[x1-xi : x2-xi+1]
      return get_max_min(subybounds)

    # given 2 corners of a rectangle, would it fit in the bound area?
    def inbounds(p1,p2) -> bool:
      x1, x2 = (p1[0], p2[0]) if p1[0]<p2[0] else (p2[0], p1[0])
      y1, y2 = (p1[1], p2[1]) if p1[1]<p2[1] else (p2[1], p1[1])
      
      xxbounds = get_xbounds(y1,y2)
      if x1 < xxbounds[0] or x2 > xxbounds[1]: return False
      yybounds = get_ybounds(x1,x2)
      if y1 < yybounds[0] or y2 > yybounds[1]: return False
      return True
    
    def printbounds(bounds):
      ci = min([range_[0] for range_ in bounds])
      cf = max([range_[1] for range_ in bounds])
      size = cf-ci+1
      print(f'{ci=}, {cf=}, {size=}')
      grid = [['.' for __ in range(size)] for _ in range(len(bounds))]
      for i, range_ in enumerate(bounds):
        c1, c2 = range_
        for j in range(c1-ci, c2-ci+1):
          grid[i][j] = 'O'
      for row in grid:
        print(row)

    # AREA CALCULATIONS ####################################################
    # print('xbounds: ',xbounds)
    # print('ybounds: ',ybounds)
    processed = 0
    largest = 0
    for i in range(n):
      for j in range(i+1,n):
        # print('\n',input[i], input[j])

        # if inbounds(input[i],input[j]):
        #   largest = max(largest, get_area(input[i], input[j]))
        
        area = get_area(input[i], input[j])
        if area > largest and inbounds(input[i],input[j]):
          largest = area
        
        processed += 1
        if processed%100==0: print(f'{processed=}, {largest=}')
    print(largest)

if __name__ == '__main__':
  example = [ # (x,y)
    (7,1),
    (11,1),
    (11,7),
    (9,7),
    (9,5),
    (2,5),
    (2,3),
    (7,3)
  ]

  example = [list(ex) for ex in example]
  # main1(example) # ans 50
  # main1()
  # main2(example) # ans 24
  main2()