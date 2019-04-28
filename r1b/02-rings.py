import sys

def find_initial(max_queries):
    print(6)
    rings_after_6 = int(input())
    print(50)
    rings_after_50 = int(input())

    dividers = [2**50, 33554432, 65536, 4096, 1024, 256]
    rings = []
    rem = rings_after_50
    for div in dividers:
        rings.append( rem // div )
        # print("got {}, going to {}".format(rings[-1], rem))
        rem = rem % div
        # print("got {}, going to {}".format(rings[-1], rem))
    
    # at this point, rings[1] and rings[2] are solid
    # rings 3-6 are maxima?
    
    nr3 = lambda rings_after, num_rings: rings_after[3] - rings_after[2] - (4*num_rings[1])
    nr4 = lambda rings_after, num_rings: rings_after[4] - rings_after[3] - (8*num_rings[1]) - (2*num_rings[2])
    nr5 = lambda rings_after, num_rings: rings_after[5] - rings_after[4] - (16*num_rings[1])
    nr6 = lambda rings_after, num_rings: rings_after[6] - rings_after[5] - (32*num_rings[1]) - (4*num_rings[2]) - (2*num_rings[3])

    base = 64*rings[0] + 8*rings[1] 
    for r3 in range(1, rings[2]+1):
        for r4 in range(1, rings[3]+1):
            for r5 in range(1, rings[4]+1):
                for r6 in range(1, rings[5]+1):
                    num_rings = base + 4*r3 + 2*r4 + 2*r5 + 2*r6
                    if num_rings == rings_after_6:
                        print("{} {} {} {} {} {}".format(rings[0], rings[1], r3,r4,r5,r6))
                        return

    print("{} {} {} {} {} {}".format(*rings))

if __name__ == "__main__":
    num_cases,max_queries = [int(i) for i in input().split(" ")]
    case_num = 1
    while case_num <= num_cases:
        find_initial(max_queries)
        result = int(input())
        if result == -1:
            sys.exit(1)
        case_num += 1