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
            if move[0] == "L": # move left
                started_at_0 = position==0
                # python mod quirk; moving left from 0 automatically gives -1
                # ex. from 0: L3->-1, L100->-1, L101->-2
                # should be L3->0, L100->-1, L101->-1
                position -= spaces
                num_0 += abs(position//100) if not started_at_0 else\
                    abs(position)//100
                if abs(position)%100 == 0: num_0 += 1
            else: # move right
                position += spaces
                num_0 += position//100
            position %= 100
            if example: print(f'moved {move} to {position}; {num_0}')

        print('ans', num_0)

if __name__ == '__main__':
    # main(["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"])
    # main(["R1000","L1000","L50","R1","L1","L1","R1","R100","R1"])
    main() # ans 6561 accepted