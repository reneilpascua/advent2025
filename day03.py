from typing import Optional, List

def main1(example: Optional[List[str]] = None):
    def get_largest_2digit(numstr) -> int:
        # either run through twice to get tens and ones
        # or do something smart and only go through one time
        n = len(numstr)
        i = n-2
        largest_up_to_i = numstr[i]
        largest_right_of_i = numstr[i+1]
        ones_ptr = i+1
        while i >= 0:
            if numstr[i] >= largest_up_to_i:
                largest_up_to_i = numstr[i]
                largest_right_of_i = numstr[ones_ptr]
            if numstr[i] > numstr[ones_ptr]:
                ones_ptr = i
            i -= 1
        return int(largest_up_to_i + largest_right_of_i)


    with open('./day03_input.txt') as f:
        # input = f.read() if not example else example
        input = [line.strip() for line in f.readlines()] if not example else example
        total_joltage = 0
        for bank in input:
            largest = get_largest_2digit(bank)
            total_joltage += largest
        print(total_joltage)
    
def main2(example: Optional[List[str]] = None):
    def get_left_largest_index(bank, l, r) -> int:
        largest = "0"
        largest_index = -1
        for i in range(l,r):
            if bank[i] > largest:
                largest = bank[i]
                largest_index = i
        return largest_index

    def get_largest_joltage(num_bats, bank):
        n = len(bank)
        bats = ''
        bats_selected = 0
        l = 0
        r = n-(num_bats-bats_selected-1)
        while bats_selected < num_bats:
            r = n-(num_bats-bats_selected-1)
            left_largest_index = get_left_largest_index(bank,l,r)
            bats += bank[left_largest_index]

            bats_selected += 1
            l = left_largest_index+1
            r = n-(num_bats-bats_selected-1)

        return int(bats)

    with open('./day03_input.txt') as f:
        # input = f.read() if not example else example
        input = [line.strip() for line in f.readlines()] if not example else example
        total_joltage = 0
        for bank in input:
            largest = get_largest_joltage(12, bank)
            # print(largest)
            total_joltage += largest
        print(total_joltage)

if __name__ == '__main__':
    example = ["987654321111111","811111111111119","234234234234278","818181911112111"]
    example2 = ["5312224222713236213232382221222222216232352633323322223233232333323422323225662322323723232222222232","3156557564452635362717784672442615553635257743349535442676644432474552623544224472653952463455546442"]
    # main1(example2)
    # main1()
    # main2(example)
    main2()