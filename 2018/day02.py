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
    with open('2018/input02.txt', 'r') as file:
        for line in file:
            if len(line) > 0:
                input.append(line)

def part1():
    twice_count = 0
    three_times_count = 0
    for line in input:
        twice_seen = False
        three_times_seen = False
        count = {} # map a character to its count

        for char in line:
            if char != '\n':
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
        
        for key in count:
            if count[key] == 2 and not twice_seen:
                twice_count += 1
                twice_seen = True
            if count[key] == 3 and not three_times_seen:
                three_times_count += 1
                three_times_seen = True
            if twice_seen and three_times_seen:
                break

    print(twice_count * three_times_count)

def part2():
    # Remove a character at cpos from all strings.
    # If there are two strings that are the same after
    # the character is removed, we've found the name.
    # Otherwise, record the name.
    # Credit: learned from @lizthegrey
    for cpos in range(len(input[0])):
        names = set()
        for lpos in range(len(input)):
            line = input[lpos]
            name = line[0:cpos] + line[cpos+1:]
            if name in names:
                print(name)
                return
            else:
                names.add(name)

main()
