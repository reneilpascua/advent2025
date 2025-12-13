from typing import Optional, List, Tuple

def main1(example: Optional[List[str]] = None):
    with open('./day04_input.txt') as f:
        input = [line.strip() for line in f.readlines()] if not example else example
        # assume all lines are the same length
        m,n = len(input), len(input[0])
        movable = 0
        for i in range(m):
            for j in range(n):
                if input[i][j] != "@": continue
                positions = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
                obstacles = 0
                for x,y in positions:
                    if (0<=x<m) and (0<=y<n) and input[x][y] == "@": obstacles += 1
                if obstacles < 4:
                    # print(i,j)
                    movable += 1
        print(movable)

def main2(example: Optional[List[str]] = None):

    def update(grid: List[List[str]], indices_to_remove: List[Tuple[int,int]]):
        for i,j in indices_to_remove:
            grid[i][j] = "."

    with open('./day04_input.txt') as f:
        pre_input: List[str] = [line.strip() for line in f.readlines()] if not example else example
        # turn into a grid of chars
        input: List[List] = [[c for c in row] for row in pre_input]
        # assume all lines are the same length
        m,n = len(input), len(input[0])
        movable = 0
        while True: # exits when there are no removables
            removables = []
            for i in range(m):
                for j in range(n):
                    if input[i][j] != "@": continue
                    positions = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
                    obstacles = 0
                    for x,y in positions:
                        if (0<=x<m) and (0<=y<n) and input[x][y] == "@": obstacles += 1
                    if obstacles < 4:
                        removables.append((i,j))
                        movable += 1
            if not removables: break
            update(input, removables)
        print(movable)

if __name__ == '__main__':
    example = ["..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]
    # main1(example)
    # main1() # ans 1523 accepted
    # main2(example)
    main2()