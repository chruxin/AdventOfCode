import datetime
import re

input = []  # a list of Events


class Event:
    def __init__(self, year, month, day, hour, minute, text):
        self.date = datetime.datetime(year, month, day, hour, minute)
        self.text = text


def main():
    parse_input()
    solve()


def parse_input():
    with open('2018/input04.txt', 'r') as file:
        for line in file:
            if len(line) > 0:
                match = re.match(
                    r"\[(?P<year>\d{4})\-(?P<month>\d{2})\-(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2})\] (?P<text>.*)\n",
                    line)
                e = Event(
                    int(match.group('year')),
                    int(match.group('month')),
                    int(match.group('day')),
                    int(match.group('hour')),
                    int(match.group('minute')),
                    match.group('text'))
                input.append(e)
        input.sort(key=lambda e: e.date)


def solve():
    guard_id = None
    prev_date = None
    record = {}  # map a guard_id to a list that represents their sleep schedule
    for e in input:
        match = re.match(r".*#(?P<guard_id>\d+).*", e.text)
        if match is not None:
            guard_id = match.group('guard_id')
            if guard_id not in record:
                record[guard_id] = [0 for _ in range(60)]
            prev_date = e.date
            continue

        if e.text == 'falls asleep':
            prev_date = e.date
        elif e.text == 'wakes up':
            # mark the time slept
            schedule = record[guard_id]
            record[guard_id] = schedule[0:prev_date.minute] + \
                [x + 1 for x in schedule[prev_date.minute:e.date.minute]] \
                + schedule[e.date.minute:]
            prev_date = e.date

    # get the guard with the most sleep time
    max_sum_sleep = 0
    sleepy_guard = None
    for guard_id in record:
        sum_sleep = sum(record[guard_id])
        if sum_sleep > max_sum_sleep:
            max_sum_sleep = sum_sleep
            sleepy_guard = guard_id

    schedule = record[sleepy_guard]
    max_minute = schedule.index(max(schedule))

    print('[part1] guard: %s, minute: %d, multiply: %d' %
          (sleepy_guard, max_minute, int(sleepy_guard) * max_minute))

    # get the max sleep and the minute of each guard
    max_sleep = 0
    max_sleep_minute = 0
    max_sleep_guard_id = 0
    for guard_id in record:
        schedule = record[guard_id]
        curr_max_sleep = max(schedule)
        if curr_max_sleep > max_sleep:
            max_sleep_minute = schedule.index(curr_max_sleep)
            max_sleep = curr_max_sleep
            max_sleep_guard_id = guard_id

    print(
        '[part2] guard: %s, minute: %d, multiply: %d' %
        (max_sleep_guard_id, max_sleep_minute, int(max_sleep_guard_id) *
         max_sleep_minute))


main()
