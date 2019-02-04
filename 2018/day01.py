import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', dest='part', type=int)
    args = parser.parse_args()
    if args.part == 1:
        part1()
    elif args.part == 2:
        part2()

# sum
def part1():
    result = 0
    with open('2018/input01.txt', 'r') as input:
        for line in input:
            curr_num = int(line)
            result += curr_num
    print(result)

# frequency more than twice
def part2():
    result = 0
    freq = set([0])
    while True:
        with open('2018/input01.txt', 'r') as input:
            for line in input:
                curr_num = int(line)
                result += curr_num
                if result in freq:
                    print(result)
                    return
                freq.add(result)

main()