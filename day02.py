from typing import Optional

def main1(example: Optional[str] = None):
    def invalid(num) -> bool:
        numstr = str(num)
        n = len(numstr)
        if n%2!=0: return False
        ans = numstr[:n//2] == numstr[n//2:]
        # if ans: print(numstr)
        return ans

    with open('./day02_input.txt') as f:
        input = f.read() if not example else example
        ranges = [ [int(item) for item in inputrange.split('-')] for inputrange in input.split(',')]
        invalids = []
        for range_ in ranges:
            for num in range(range_[0], range_[-1]+1):
                if invalid(num): invalids.append(num)
            # print(range_, len(invalids))
        print(sum(invalids))

def main2(example: Optional[str] = None):    
    def invalid(num) -> bool:
        numstr = str(num)
        n = len(numstr)
        howmany = 2 # number of pieces into which to split numstr
        while howmany <= n:
            if n%howmany == 0:
                chunksize = n//howmany
                parts = numstr.split(numstr[:chunksize])
                if not any(parts): return True
            howmany += 1
        return False
    
    with open('./day02_input.txt') as f:
        input = f.read() if not example else example
        ranges = [ [int(item) for item in inputrange.split('-')] for inputrange in input.split(',')]
        invalids = []
        for range_ in ranges:
            for num in range(range_[0], range_[-1]+1):
                if invalid(num): invalids.append(num)
            # print(range_, len(invalids))
        print(sum(invalids))

if __name__ == '__main__':
    example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    # main1(example)
    # main1()
    # main2(example)
    main2() # ans 30260171216 accepted