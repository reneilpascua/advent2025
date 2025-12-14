from typing import Optional, List

def main1(example: Optional[List[str]] = None):
    with open('./day07_input.txt') as f:
        input: List[str] = f.readlines() if not example else example
        # NOTE: guaranteed no splitters at edges

        beams: List[int] = [input[0].index('S')] # position of beams
        
        def add_to_beams_(beams_,pos):
            if not beams_ or beams_[-1]!=pos: beams_.append(pos)

        times_split = 0
        for row in input:
            beams_=[]
            for beam in beams:
                if row[beam]=='^':
                    times_split += 1
                    add_to_beams_(beams_, beam-1)
                    add_to_beams_(beams_, beam+1)
                else:
                    add_to_beams_(beams_, beam)
                beams = beams_
        print(times_split)

def main2_recursive(example: Optional[List[str]] = None):
    with open('./day07_input.txt') as f:
        input: List[str] = f.readlines() if not example else example
        # NOTE: guaranteed no splitters at edges

        # truncate input
        # input = input[:60]

        start = input[0].index('S') # position of beam
        n = len(input)

        num_timelines = 0
        times_called = 0
        def traverse(t, pos):
            nonlocal num_timelines, n, input, times_called
            times_called += 1
            if t == n: # reached the end
                num_timelines += 1
                return
            if input[t][pos]=='^':
                traverse(t+1,pos-1)
                traverse(t+1,pos+1)
            else:
                traverse(t+1, pos)
        traverse(1, start)
        print(f'{times_called=}')
        print(num_timelines)

# iterative
def main2(example: Optional[List[str]] = None):
    with open('./day07_input.txt') as f:
        input: List[str] = f.readlines() if not example else example
        # NOTE: guaranteed no splitters at edges
        
        # truncate input for testing
        # input = input[:3]

        # dp[i] is how many ways a tachyon land at i
        dp = [0 for _ in range(len(input[0]))]
        dp[ input[0].index('S') ] = 1

        for row in input[1:]:
            dp_ = [0 for _ in range(len(row))]
            for i in range(len(row)):
                t_i = dp[i]
                if row[i]=='^':
                    dp_[i-1] += t_i
                    dp_[i+1] += t_i
                else:
                    dp_[i] += t_i
            dp = dp_
        print(sum(dp))

if __name__ == '__main__':
    example = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "..............."
    ]
    example2 = [
        '...S.',
        '...^.',
        '..^..',
        '.^.^.',
    ]
    # main1(example)
    # main1() # ans 1698 accepted
    # main2(example)

    # recursive was not the right way to do this bc
    # there were multiple ways for a tach to arrive at i
    # -> use iterative dp sol
    main2() # ans 95408386769474 accepted