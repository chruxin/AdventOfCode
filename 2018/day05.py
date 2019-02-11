import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--part', dest='part', type=int)
    args = parser.parse_args()
    if args.part == 1 or args.part == 2:
        input = parse_input()

    if args.part == 1:
        part1(input)
    elif args.part == 2:
        part2()


def parse_input():
    with open('2018/input05.txt', 'r') as file:
        input = file.read().strip()
    return input


def react(char1, char2):
    return char1 != char2 and char1.upper() == char2.upper()


# Only iterate over the input string once.
# When a reaction is found, check their pairs of neighbors
# to see if they react too.
# This is much, MUCH faster than the brute force solution,
# which is to iterate the input over and over again until
# no new reaction is found.
def part1(input):
    # accumulator: the result string so far from the left of input
    str = ''
    i = 0
    while i < len(input):
        if i == len(input) - 1:
            # last character
            str = str + input[i]
            break
        if react(input[i], input[i+1]):
            # two characters react
            # check if more reactions can happen after current pair destroys

            # to the left, we have str[len(str)-2] --> str[0]
            num_left = len(str)
            # to the right, input[i+2] --> input[len(input)-1]
            num_right = len(input) - (i + 2)
            # number of pairs we need to check for reaction
            num = min(num_left, num_right)
            left = len(str) - 1
            right = i + 2
            # new accumulator so that we don't mess up the 
            # indices while removing chars
            new_str = str
            #                               pairs of reactions
            #                        |--------------------------------|
            #                             |----------------------|
            #                                  |------------|
            #  [ ............ str ............ _ ]   X x   [_ ............ rest of input ............]
            #                                 ⬆️    ⬆️️      ⬆️
            #                                left   i     right
            #                         |-- j --|            |-- j --|
            #                        ⬆️                             ⬆️
            #                 curr_left_index                curr_right_index
            #                                                        ⬆️
            #  [ ..... new_str .....]                             updated i
            for j in range(0, num):
                curr_left_index = left - j
                curr_right_index = right + j
                left_char = str[curr_left_index]
                right_char = input[curr_right_index]
                # check if the pair reacts
                if react(left_char, right_char):
                    # pair reacts, update new accumulator
                    # to exclude the char that reacts and
                    # update i
                    new_str = str[0:curr_left_index]
                    i = curr_right_index + 1
                else:
                    # pair doesn't react, update i and break out
                    i = curr_right_index
                    break
            # update i to skip the ones reacted
            i = max(i, right)
            str = new_str
        else:
            str += input[i]
            i += 1 
    print(len(str))


def part2():
    print('part 2')


main()
