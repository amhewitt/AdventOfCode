import re
import numpy as np

claims = [str(x) for x in open("./input/day3-input.txt").readlines()]

# Part 1

fb = np.zeros((1000, 1000))

for claim in claims:
    claim_id, start_left, start_top, width, length = map(int, re.findall(r'\d+', claim))
    fb[start_left:start_left + width, start_top:start_top + length] += 1
print(np.sum(fb > 1))

# Part 2

for claim in claims:
    claim_id, start_left, start_top, width, length = map(int, re.findall(r'\d+', claim))
    if np.all(fb[start_left:start_left + width, start_top:start_top + length] == 1):
        print(claim_id)
