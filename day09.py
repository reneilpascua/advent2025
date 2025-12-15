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
        # x means left to right, y means up and down 

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

        # for y = Y, what is the leftest and rightest x could be?
        xbounds: List[List] = [[float('inf'), float('-inf')] for _ in range(yf-yi+1)]
        # for x = X, what is the lowest and highest y could be?
        ybounds: List[List] = [[float('inf'), float('-inf')] for _ in range(xf-xi+1)]
        
        # draw the boundaries
        for i in range(1,n):
            p1, p2 = input[i-1], input[i]
            x1, x2 = (p1[0], p2[0]) if p1[0]<p2[0] else (p2[0], p1[0])
            y1, y2 = (p1[1], p2[1]) if p1[1]<p2[1] else (p2[1], p1[1])
            
            if x1==x2: # do xbounds
                for j in range(y1-yi,y2-yi+1):
                    xby = xbounds[j]
                    xby[0] = min(xby[0], x1)
                    xby[1] = max(xby[1], x2)
                ybx1 = ybounds[x1-xi]
                ybx1[0] = min(ybx1[0], y1)
                ybx1[1] = min(ybx1[1], y2)
            elif y1==y2: # do ybounds
                for j in range(x1-xi,x2-xi+1):
                    ybx = ybounds[j]
                    ybx[0] = min(ybx[0], y1)
                    ybx[1] = max(ybx[1], y2)
                xby1 = xbounds[y1-yi]
                xby1[0] = min(xby1[0], x1)
                xby1[1] = min(xby1[1], x2)
            else:
                raise Exception('one axis should be the same')

        # HELPER FUNCTIONS TO DETERMINE INBOUNDS ###############################
        def get_max_min(l) -> List:
            max_minbound = l[0][0]
            min_maxbound = l[0][1]
            for sub in l[1:]:
                max_minbound = max(l[0])
                min_maxbound = min(l[1])
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
        
        def drawbounds(bounds):
            xi = min([range_[0] for range_ in bounds])
            xf = max([range_[1] for range_ in bounds])

            size = xf-xi+1

            grid = [['.' for __ in range(size)] for _ in range(len(bounds))]
            for i, range_ in enumerate(bounds):
                x1, x2 = range_
                for j in range(x1-xi, x2-xi+1):
                    grid[i][j] = 'O'
            
            for row in grid:
                print(row)

        drawbounds(ybounds) # it looks like ybounds was done right but not xbounds
        # AREA CALCULATIONS ####################################################
        largest = 0
        for i in range(n):
            for j in range(i+1,n):
                if inbounds(input[i],input[j]):
                    print(input[i], input[j])
                    largest = max(largest, get_area(input[i], input[j]))
        print(largest)

if __name__ == '__main__':
    example = [
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