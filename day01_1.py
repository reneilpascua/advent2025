from typing import Optional, List

def main(example: Optional[List[str]] = None):
    with open('./day01_input.txt','r') as f:
        moves: List[str] = example if example else\
            [line.strip() for line in f.readlines()]
        
        # dial is 0-99 inclusive (100 entries)
        num_0 = 0
        position = 50
        for move in moves:
            spaces = int(move[1:])
            if move[0]=="L": spaces *= -1
            position += spaces
            position %= 100
            if position == 0: num_0 += 1
        print(num_0)

if __name__ == '__main__':
    main() # ans 1145 accepted