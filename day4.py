import re
from collections import defaultdict

times = [str(x) for x in open("./input/day4-input.txt").readlines()]

# Part 1

guards_by_time_slept = defaultdict(int)
times_slept_by_guard_and_minute = defaultdict(int)

for time in sorted(times): 
    """
    ISO standard date/time, so you can just sort without having to do anything fancy
    Begins shift, sleep, and wake up are the three possibilities
    Only one guard on shift at a time
    """
    if 'begins shift' in time:
        current_guard_id = int(re.findall(r'#\d+', time)[0].strip('#'))
    elif 'falls asleep' in time:
        sleep_start_time = int(re.findall(r':\d+', time)[0].strip(':')) #only minutes are relevant
    elif 'wakes up' in time:
        sleep_end_time = int(re.findall(r':\d+', time)[0].strip(':'))
        guards_by_time_slept[current_guard_id] += (sleep_end_time - sleep_start_time)
        for t in range(sleep_start_time, sleep_end_time):
            times_slept_by_guard_and_minute[(current_guard_id, t)] += 1

best_guard = max(guards_by_time_slept, key=guards_by_time_slept.get)
best_min_times = 0
best_min = 0

for i in range(60):
    if best_min_times == 0 or best_min_times < times_slept_by_guard_and_minute[(best_guard, i)]:
        best_min = i
        best_min_times = times_slept_by_guard_and_minute[(best_guard, i)]

print(best_guard * best_min)

# Part 2

best_guard, best_min = max(times_slept_by_guard_and_minute, key=times_slept_by_guard_and_minute.get)
print(best_guard * best_min)