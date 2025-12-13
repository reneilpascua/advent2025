from typing import Optional

def main(example: Optional[str] = None):
    with open('./day00_input.txt') as f:
        input = f.read() if not example else example
        # input = f.readlines() if not example else example
        # input = [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    # example = 
    # main(example)
    main()