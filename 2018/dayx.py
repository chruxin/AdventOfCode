'''Boilerplate'''

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
    with open('2018/inputx.txt', 'r') as file:
        for line in file:
            if len(line) > 0:
                input.append(line.strip())


def part1():
    print('part 1')


def part2():
    print('part 2')


main()
