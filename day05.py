from typing import Optional, List, Tuple

def main1(example: Optional[List[str]] = None):
    def simplify_intervals(intervals_str) -> List[List[int]]:
        intervals: List[List[int]] = [[int(end) for end in interval_str.split('-')] for interval_str in intervals_str]
        intervals.sort(key = lambda x:x[0])

        simplified = [intervals[0]]
        for interval in intervals[1:]:
            last = simplified[-1]
            if interval[0] <= last[1]: # overlaps
                simplified[-1][1] = max(last[1], interval[1])
            else: # new interval
                simplified.append(interval)
        
        return simplified

    def in_interval(num,interval): return interval[0]<=num<=interval[1]

    def search_intervals(id:int, intervals:List[List[int]]) -> bool:
        l,r = 0, len(intervals)-1
        while l<=r:
            m=(l+r)//2
            interval = intervals[m]
            if in_interval(id, interval):
                return True
            elif id < interval[0]:
                r=m-1
            elif id > interval[1]:
                l=m+1
        return False

    
    with open('./day05_input.txt') as f:
        input = [line.strip() for line in f.readlines()] if not example else example
        
        intervals_str = []
        i=0
        while input[i]: # stops at the blank line
            intervals_str.append(input[i])
            i += 1
        ids_str = [line for line in input[i+1:]]

        intervals = simplify_intervals(intervals_str)
        fresh = 0
        for id_str in ids_str:
            if search_intervals(int(id_str), intervals): fresh += 1
        print(fresh)

def main2(example: Optional[List[str]] = None):
    def simplify_intervals(intervals_str) -> List[List[int]]:
        intervals: List[List[int]] = [[int(end) for end in interval_str.split('-')] for interval_str in intervals_str]
        intervals.sort(key = lambda x:x[0])

        simplified = [intervals[0]]
        for interval in intervals[1:]:
            last = simplified[-1]
            if interval[0] <= last[1]: # overlaps
                simplified[-1][1] = max(last[1], interval[1])
            else: # new interval
                simplified.append(interval)
        
        return simplified

    def in_interval(num,interval): return interval[0]<=num<=interval[1]

    def search_intervals(id:int, intervals:List[List[int]]) -> bool:
        l,r = 0, len(intervals)-1
        while l<=r:
            m=(l+r)//2
            interval = intervals[m]
            if in_interval(id, interval):
                return True
            elif id < interval[0]:
                r=m-1
            elif id > interval[1]:
                l=m+1
        return False

    
    with open('./day05_input.txt') as f:
        input = [line.strip() for line in f.readlines()] if not example else example
        
        intervals_str = []
        i=0
        while input[i]: # stops at the blank line
            intervals_str.append(input[i])
            i += 1
        # ids_str = [line for line in input[i+1:]]

        intervals = simplify_intervals(intervals_str)
        # fresh = 0
        # for id_str in ids_str:
        #     if search_intervals(int(id_str), intervals): fresh += 1
        # print(fresh)
        fresh_ids = 0
        for interval in intervals:
            fresh_ids += interval[1]-interval[0]+1
        print(fresh_ids)

if __name__ == '__main__':
    example = ["3-5","10-14","16-20","12-18","","1","5","8","11","17","32"]
    main1(example)
    main1() # ans 888 accepted
    main2() # ans 344378119285354 accepted