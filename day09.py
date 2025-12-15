from typing import Optional, Tuple, List

def get_area(p1: List[int], p2: List[int]) -> int:
    x, y = abs(p2[0]-p1[0])+1, abs(p2[1]-p1[1])+1
    return x*y

def main1(example: Optional[List[List[int]]] = None):
    with open('./day09_input.txt') as f:
        input = [[int(d) for d in line.split(',')] for line in f.readlines()] if not example else example

        # naive soln: compare all points to each other O(n^2)
        n = len(input)
        largest = 0
        for i in range(n):
            for j in range(i+1,n):
                largest = max(largest, get_area(input[i], input[j]))
        print(largest)

        # according to chatgpt, u would use "convex hull" for this...
        # which isn't really leetcode/interview friendly



if __name__ == '__main__':
    example = [
        (7,1),
        (11,1),
        (11,7),
        (9,7),
        (9,5),
        (2,5),
        (2,3),
        (7,3)
    ]

    example = [list(ex) for ex in example]
    # main1(example) # ans 50
    # main1()
    # main2(example) # ans 24