from itertools import cycle

# Part 1

freqs = [int(x) for x in open("./input/day1-input.txt").readlines()]
print(sum(freqs))

# Part 2

current_frequency = 0
freqs_so_far = {0}

for x in cycle(freqs):
    current_frequency += x
    if current_frequency in freqs_so_far:
        print(current_frequency , "is the repeated number")
        break
    freqs_so_far.add(current_frequency)