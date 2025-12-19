from typing import Optional, TextIO, List, Tuple


def process_input(f: TextIO) -> List[List[int]]:
    return [[int(d) for d in line.split(',')] for line in f.readlines()]

def get_area(p1: List[int], p2: List[int]) -> int:
  x, y = abs(p2[0]-p1[0])+1, abs(p2[1]-p1[1])+1
  return x*y

# def get_candidates(data):
#     n = len(data)
#     sorteddata = sorted(data, key=lambda x: (x[0], x[1]))
#     num_candidates = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             if sorteddata[j][1]>=sorteddata[i][1]:
#                 num_candidates += 1
    
#     print(f'max number of pair combinations: {n*(n-1)//2}')
#     print(f'actual candidate pairs: {num_candidates}')


def get_offsets(data) -> Tuple[int, int, int, int]:
    """gets the 4 corners of our solution space"""
    xi = min([p[0] for p in data])
    xf = max([p[0] for p in data])
    yi = min([p[1] for p in data])
    yf = max([p[1] for p in data])
    return xi,xf,yi,yf

def draw_line(grid,x1,x2,y1,y2):
    """draws a line on grid using OFFSET coordinates"""
    if x1==x2:
        for i in range(y1,y2+1): grid[i][x1] = 1
    elif y1==y2:
        for i in range(x1,x2+1): grid[y1][i] = 1
    else: raise Exception("one of x or y must be same")

def fill_grid(grid: List[List[int]]):
    m,n = len(grid), len(grid[0])
    visited = [[0 for _ in range(n)] for __ in range(m)]

    def flood_fill(i,j):
        nonlocal m,n,visited
        if not ((0<=i<m) and (0<=j<n)): return # oob
        if visited[i][j] or grid[i][j]: return # dont fill

        visited[i][j] = 1
        for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            flood_fill(i+di,j+dj)
    
    # flood_fill from boundary
    for i in range(m):
        flood_fill(i,0)
        flood_fill(i,n-1)
    for j in range(n):
        flood_fill(0,j)
        flood_fill(m-1,j)

    # fill interior
    for i in range(m):
        for j in range(n):
            if not grid[i][j] and not visited[i][j]:
                grid[i][j] = 1

def get_grid(data, xi, xf, yi, yf) -> List[List[int]]:
    """draws the 2d space according to where the red rectangle can be"""
    print(f'size: {xf-xi+1} X {yf-yi+1}')
    grid = [[0 for _ in range(xf-xi+1)] for __ in range(yf-yi+1)] # this is way too big
    print('init grid')
    # use data to draw outline
    for i in range(len(data)):
        p1, p2 = data[i-1], data[i]
        x1, x2 = (p1[0], p2[0]) if p1[0]<p2[0] else (p2[0], p1[0])
        y1, y2 = (p1[1], p2[1]) if p1[1]<p2[1] else (p2[1], p1[1])
        draw_line(grid, x1-xi, x2-xi, y1-yi, y2-yi)
    print('drew outline')

    # fill in the center
    fill_grid(grid)
    print('filled')
    return grid

def inbounds(grid, di, dj, xi, yi) -> bool:
    # values of dj guaranteed to be greater or equal to values of di
    x1, x2 = di[0]-xi, dj[0]-xi
    y1, y2 = di[1]-yi, dj[1]-yi
    for x in range(x1, x2+1):
        if not grid[y1][x]: return False
    for x in range(x1, x2+1):
        if not grid[y2][x]: return False
    for y in range(y1,y2+1):
        if not grid[y][x1]: return False
    for y in range(y1,y2+1):
        if not grid[y][x2]: return False

    return True

def solve(data) -> int:
    # our offset 2d space
    corners = get_offsets(data) # xi, xf, yi, yf
    print('corners')
    grid: List[List[int]] = get_grid(data, *corners)
    print('grid')
    
    data.sort(key=lambda x:(x[0],x[1])) # sort by x,y and only make rects w >x,>y
    print('sorted')
    n = len(data)
    largest = 0
    processed = 0
    for i in range(n):
        for j in range(i+1,n):
            di, dj = data[i], data[j]
            if dj[1] > di[1]:
                area = get_area(di,dj)
                if area > largest and inbounds(grid,di,dj,corners[0],corners[2]):
                    largest = area
                
            processed += 1
            if processed % 100 == 0: print(f'processed {processed}')
    return largest

def main(example: Optional[List[List[int]]] = None):
    with open('./day09_input.txt') as f:
        data: List[List[int]] = process_input(f) if not example else example
        print(solve(data))

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
    example2 = [
        (1,1),
        (1,20),
        (5,20),
        (5,17),
        (3,17),
        (3,14),
        (5,14),
        (5,10),
        (3,10),
        (3,6),
        (5,6),
        (5,1)
    ]
    example2 = [list(ex) for ex in example2]
    # main(example)
    main()