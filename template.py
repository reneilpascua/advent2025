from typing import Optional, TextIO

def process_input(f: TextIO): # choose the appropriate return for the input
    return f.read()
    return f.readlines()
    return [line.strip() for line in f.readlines()]

def solve1(data):
    pass

def solve2(data):
    pass

def main(example: Optional[str] = None):
    with open('./day00_input.txt') as f:
        data = process_input(f) if not example else example
        print(solve1(data))
        # print(solve2(data))

if __name__ == '__main__':
    example = None
    main(example)
    # main()