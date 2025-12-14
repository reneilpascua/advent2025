from typing import Optional, List

def reduce(items: List[int], op: str) -> int:
    return multiply(items) if op=='*' else add(items)

def multiply(items: List[int]) -> int:
    result = 1
    for item in items: result *= item
    return result

def add(items: List[int]) -> int:
    result = 0
    for item in items: result += item
    return result

def main1(example: Optional[List[str]] = None):
    with open('./day06_input.txt') as f:
        input = [line.strip() for line in f.readlines()] if not example else example
        input = [line.split() for line in input]
        m, n = len(input), len(input[0])

        ops = input[-1]
        anses: List[int] = []
        for j in range(n):
            op: str = ops[j]
            operands: List[int] = []
            for i in range(m-1):
                operands.append(int(input[i][j]))
            anses.append(reduce(operands, op))
        print(sum(anses))

def main2(example: Optional[List[str]] = None):
   with open('./day06_input.txt') as f:
        input = f.readlines() if not example else example
        
        # figure out the index at which each column ends
        ops_str = input[-1]
        ends = [-2]
        i = 1 # we know the 0th element is an operation
        while i < len(ops_str):
            if ops_str[i] != ' ':
                ends.append(i-2)
            i += 1
        ends.append(len(ops_str)-1)

        ops = ops_str.split()
        anses: List[int] = []
        for col_index in range(len(ops)):
            operands = []
            for j in range(ends[col_index+1], ends[col_index]+1,-1):
                operand = ''
                for i in range(len(input)-1):
                    c = input[i][j]
                    if c!=' ': operand+=c
                operands.append(int(operand))
            anses.append(reduce(operands, ops[col_index]))
        print(sum(anses))

if __name__ == '__main__':
    example = [
        '123 328  51 64 ',
        ' 45 64  387 23 ',
        '  6 98  215 314',
        '*   +   *   +  '
    ]
    # main1(example)
    # main1() # ans 5322004718681 accepted
    # main2(example)
    main2() # ans 9876636978528 accepted
