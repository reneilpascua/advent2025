from typing import Optional, Tuple

def get_area(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    x, y = abs(p2[0]-p1[0])+1, abs(p2[1]-p1[1])+1
    return x*y

if __name__=='__main__':
    p1, p2 = (1,1), (5,8)
    print(get_area(p1,p2))
