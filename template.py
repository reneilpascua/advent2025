from typing import Optional, TextIO

def process_input(f: TextIO): # choose the appropriate return for the input
    return f.read()
    return f.readlines()
    return [line.strip() for line in f.readlines()]

def main1(example: Optional[str] = None):
    with open('./day00_input.txt') as f:
        input = process_input(f) if not example else example

if __name__ == '__main__':
    # example = 
    # main1(example)
    main1()