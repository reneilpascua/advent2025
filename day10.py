from typing import Optional, List, Tuple, Dict
from collections import deque

def split_manual(manual: str) -> Tuple:
    """returns the on-config and the possible operations"""
    manual_ = manual.split(' ')
    on_config = manual_[0]
    state = ''.join(['1' if c=='#' else '0' for c in on_config[1:-1]])
    ops = []
    for op in manual_[1:-1]:
        op_ = op.split(',')
        op_[0] = op_[0][1:]
        op_[-1] = op_[-1][:-1]
        ops.append([ int(c) for c in op_ ])
    return state, ops

def build_mask(op: List[int], length: int) -> int:
    mask = 0
    for i in op:
        mask |= 1 << (length-1-i)
    return mask # apply mask by doing num^mask

def solve(state: str, ops: List[List[int]]) -> int:
    length = len(state)
    target = int(state, 2) # convert to int 
    if target == 0: return 0

    masks = [build_mask(op, length) for op in ops]
    
    # bfs - guaranteed shortest first
    visited = set()
    q = deque( [(target^mask, i) for i, mask in enumerate(masks)] )
    presses = 0
    while q:
        presses += 1
        for _ in range(len(q)):
            st, mask_i = q.popleft()
            if (st, mask_i) in visited: continue
            if not st: return presses
            for j in range(mask_i+1, len(masks)):
                q.append( (st^masks[j], j) )
            visited.add((st, mask_i))
    raise Exception('unreachable state')

def main1(example: Optional[List[str]] = None):
    with open('./day10_input.txt') as f:
        input: List[str] = f.readlines() if not example else example

        presses = 0
        for manual in input:
            presses += solve(*split_manual(manual))
        print(presses)




if __name__ == '__main__':
    example = ["[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"]
    example_05 = ["[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"]
    example1 = [
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    ]
    # main1(example1)
    main1() # ans 505 accepted