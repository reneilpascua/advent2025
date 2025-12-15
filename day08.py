from typing import Optional, List, Set, Tuple, Dict
from heapq import heappop, heappush, heapify

def distance(c1, c2):
    return sum( [(c1[0]-c2[0])**2, (c1[1]-c2[1])**2, (c1[2]-c2[2])**2] )

def main1(to_process: int, example: Optional[List[List[int]]] = None):
    with open('./day08_input.txt') as f:
        input = [[int(c) for c in line.split(',')] for line in f.readlines()] if not example else example
        
        # populate distance heap: O(n^2) + O(n)
        n: int = len(input)
        d: List[Tuple] = [] # heap of distances and indices
        for i in range(n): # O(n)
            for j in range(i+1,n): # O(n)
                d.append((distance(input[i],input[j]),i,j))
        heapify(d) # O(n)

        # create connections
        seen: Set = set()
        circuits: Dict[int,Set] = dict()

        def find_circuit(a: int) -> int:
            """
            finds the key of the set in `circuits` that contains `a`.
            returns -1 if unfound
            """
            nonlocal circuits
            for k,v in circuits.items():
                if a in v: return k
            return -1


        def add_to_circuit(a: int, b: int) -> None:
            """
            adds `b` to to the same set that contains `a`.
            """
            nonlocal circuits
            k = find_circuit(a)
            if k==-1: raise Exception(f'{a} not found in any circuit')
            circuits[k].add(b)

        processed = 0
        while processed < to_process and d:
            _, a, b = heappop(d)

            # case 1: a and b already seen
            if a in seen and b in seen:
                k1, k2 = find_circuit(a), find_circuit(b)
                if k1!=k2: # a,b in separate circuits -> combine circuits
                    circuits[k1] |= circuits[k2]
                    del circuits[k2]
                # else, k1==k2 -> a,b already part of the same circuit
            
            # case 2: neither a nor b have been seen
            elif a not in seen and b not in seen:
                # make a new circuit
                circuits[processed] = {a,b} # use `processed` to ensure unique key
            
            # case 3: a seen, b not seen
            elif a in seen and b not in seen:
                add_to_circuit(a,b)
            
            # case 4: b seen, a not seen
            elif a not in seen and b in seen:
                add_to_circuit(b,a)
            
            # at this point, both a and b have been seen.
            seen.add(a)
            seen.add(b)
            processed += 1
        
        # print(circuits)
        circuit_sizes = []
        for v in circuits.values():
            heappush(circuit_sizes, -len(v))
        # print(f'{sum(circuit_sizes)=}')

        product = 1
        for _ in range(3):
            product *= -heappop(circuit_sizes)
        print(product)

def main2(example: Optional[List[List[int]]] = None):
   with open('./day08_input.txt') as f:
        input = [[int(c) for c in line.split(',')] for line in f.readlines()] if not example else example
        
        # populate distance heap: O(n^2) + O(n)
        n: int = len(input)
        d: List[Tuple] = [] # heap of distances and indices
        for i in range(n): # O(n)
            for j in range(i+1,n): # O(n)
                d.append((distance(input[i],input[j]),i,j))
        heapify(d) # O(n)

        # create connections
        circuits: Dict[int,Set] = {i:{i} for i in range(n)} # in their own circs

        def find_circuit(a: int) -> int:
            nonlocal circuits
            for k,v in circuits.items():
                if a in v: return k
            raise Exception(f'{a} not found in circuits dict')


        while d:
            _, a, b = heappop(d)
            k1, k2 = find_circuit(a), find_circuit(b)
            if k1 != k2:
                circuits[k1] |= circuits[k2]
                del circuits[k2]
            if len(circuits)==1:
                print(input[a][0]*input[b][0])
                break
        
        
        # asdf

def main1_unionfind(example: Optional[List[List[int]]] = None):
    with open('./day08_input.txt') as f:
        input = [[int(c) for c in line.split(',')] for line in f.readlines()] if not example else example
        
        # populate distance heap: O(n^2) + O(n)
        n: int = len(input)
        d: List[Tuple] = [] # heap of distances and indices
        for i in range(n): # O(n)
            for j in range(i+1,n): # O(n)
                d.append((distance(input[i],input[j]),i,j))
        heapify(d) # O(n)

        parent = list(range(n))
        # print(parent)
        def find(x):
            if parent[x] == x: return x
            return find(parent[x])
    
        def union(a,b):
            ra = find(a)
            rb = find(b)
            parent[ra] = rb

        processed = 0 
        while processed < 10 and d:
            _, a, b = heappop(d)
            # print(f'uniting {a}, {b}')
            union(a,b)
            processed += 1
        
        # create actual sets (need to know sizes, instead of just belonging)
        circuits = dict()
        for i in range(n):
            par = find(i)
            if par not in circuits:
                circuits[par] = set()
            circuits[par].add(i)
        # print(circuits)
        circuit_sizes = []
        for v in circuits.values():
            heappush(circuit_sizes,-len(v))
        product = 1
        for _ in range(3):
            product *= -heappop(circuit_sizes)
        print(product)

def main2_unionfind(example: Optional[List[List[int]]] = None):
    with open('./day08_input.txt') as f:
        input = [[int(c) for c in line.split(',')] for line in f.readlines()] if not example else example
        
        # populate distance heap: O(n^2) + O(n)
        n: int = len(input)
        d: List[Tuple] = [] # heap of distances and indices
        for i in range(n): # O(n)
            for j in range(i+1,n): # O(n)
                d.append((distance(input[i],input[j]),i,j))
        heapify(d) # O(n)
        

        separate_parts = n
        parent = list(range(n))
        # print(parent)
        def find(x):
            if parent[x] == x: return x
            return find(parent[x])
    
        def union(a,b):
            nonlocal separate_parts
            ra = find(a)
            rb = find(b)
            if ra != rb:
                parent[ra] = rb
                separate_parts -= 1
        
        while d:
            _, a, b = heappop(d)
            union(a,b)
            if separate_parts == 1:
                print(input[a][0]*input[b][0])
                return
        

if __name__ == '__main__':
    example = [
        [162,817,812],
        [57,618,57],
        [906,360,560],
        [592,479,940],
        [352,342,300],
        [466,668,158],
        [542,29,236],
        [431,825,988],
        [739,650,466],
        [52,470,668],
        [216,146,977],
        [819,987,18],
        [117,168,530],
        [805,96,715],
        [346,949,466],
        [970,615,88],
        [941,993,340],
        [862,61,35],
        [984,92,344],
        [425,690,689]
    ]
    # main1(10, example)
    # main1(1000) # ans 330786 accepted
    # main2(example)
    # main2() # ans 3276581616 accepted
    main2_unionfind()
    