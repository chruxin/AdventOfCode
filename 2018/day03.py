import argparse

input = []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', dest='part', type=int)
    args = parser.parse_args()
    if args.part == 1 or args.part == 2:
        parse_input()

    if args.part == 1:
        part1()
    elif args.part == 2:
        part2()


def parse_input():
    with open('2018/input03.txt', 'r') as file:
        for line in file:
            if len(line) > 0:
                input.append(line.strip())


def part1():
    # handy way to represent a matrix without
    # initializing it
    space = {}
    result = 0
    for line in input:
        at = line.find('@')
        period = line.find(',')
        colon = line.find(':')
        times = line.find('x')
        col = int(line[at+2:period])
        row = int(line[period+1:colon])
        width = int(line[colon+2:times])
        height = int(line[times+1:])
        for i in range(row, row + height):
            for j in range(col, col + width):
                if (i, j) not in space:
                    space[i, j] = 1
                elif space[i, j] == 1:
                    # already occupied
                    result += 1
                    space[i, j] += 1
    print(result)


def part2():
    space = {}
    claims = {} # map an ID to if it overlaps
    for line in input:
        at = line.find('@')
        period = line.find(',')
        colon = line.find(':')
        times = line.find('x')
        id = int(line[1:at])
        col = int(line[at+2:period])
        row = int(line[period+1:colon])
        width = int(line[colon+2:times])
        height = int(line[times+1:])
        overlap = False
        for i in range(row, row + height):
            for j in range(col, col + width):
                if (i, j) not in space:
                    # mark (i, j) with id
                    space[i, j] = id
                elif space[i, j] > 0:
                    overlap_id = space[i, j]
                    # mark the old id as overlapped
                    claims[overlap_id] = True
                    overlap = True
                    space[i, j] = id
        claims[id] = overlap

    # in the end, find the id that does not overlap
    for id in claims:
        if not claims[id]:
            print(id)
            return


main()
