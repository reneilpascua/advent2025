from typing import Optional, List, Dict, TextIO
from functools import cache

def process_input(f: TextIO) -> Dict[str,List[str]]: # choose the appropriate return for the input
    lines = [line.strip() for line in f.readlines()]
    keys, vals = [], []
    for line in lines:
        newline = line.split(':')
        keys.append(newline[0])
        vals.append(newline[1].strip().split(' '))
    return {key: val for key, val in zip(keys, vals)}

def solve1(data: Dict[str,List[str]]) -> int:
    count = 0
    def dfs(node):
        nonlocal count
        if node == "out":
            count += 1
        else:
            for outbound in data[node]:
                dfs(outbound)
    dfs("you")
    return count

def solve2(data: Dict[str,List[str]]) -> int:
    
    seen = set()
    @cache
    def dfs(node, dac, fft):
        nonlocal seen

        state = (node, dac, fft)
        if state in seen: raise Exception("infinite number of valid paths")

        if node == "out": return 1 if (dac and fft) else 0 # int(dac and fft)
        
        seen.add(state)
        count = 0
        for outb in data.get(node, []):
            count += dfs(outb, dac or node=="dac", fft or node=="fft")
        seen.remove(state)
        return count
    
    return dfs("svr", False, False)

def main(example: Optional[Dict[str,List[str]]] = None):
    with open('./day11_input.txt') as f:
        data = process_input(f) if not example else example
        # print(solve1(data)) # ans 719 accepted
        print(solve2(data)) # ans 27 not accepted...

if __name__ == '__main__':
    example_ = {
        "aaa": "you hhh",
        "you": "bbb ccc",
        "bbb": "ddd eee",
        "ccc": "ddd eee fff",
        "ddd": "ggg",
        "eee": "out",
        "fff": "out",
        "ggg": "out",
        "hhh": "ccc fff iii",
        "iii": "out",
    }
    example2_ = {
        "svr": "aaa bbb",
        "aaa": "fft",
        "fft": "ccc",
        "bbb": "tty",
        "tty": "ccc",
        "ccc": "ddd eee",
        "ddd": "hub",
        "hub": "fff",
        "eee": "dac",
        "dac": "fff",
        "fff": "ggg hhh",
        "ggg": "out",
        "hhh": "out"
    }
    example = {key: val.split(" ") for key, val in example_.items()}
    example2 = {key: val.split(" ") for key, val in example2_.items()}
    # main(example2)
    main()