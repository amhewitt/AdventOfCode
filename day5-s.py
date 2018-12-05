# An attempt to make my solution to AoC's Day 5 puzzle run faster by treating the strings as a stack instead.
# day5.py's part B takes about 50 minutes to complete, this one takes about a second.

rxn = [str(x) for x in open("./input/day5-input.txt").readlines()][0].strip('\n')

# Part 1

mrxn = rxn
ongoing_count = []

for r in mrxn:
    if not ongoing_count:
        ongoing_count.append(r)
    else:
        comp_char = ongoing_count[-1]

        if ord(comp_char) - ord(r) == 32 or ord(comp_char) - ord(r) == -32:
            ongoing_count.pop()
        else:
            ongoing_count.append(r)

print(len(ongoing_count))

# Part 2

mrxn = rxn
shortest = len(mrxn)
ongoing_count = []
alphas = "qwertyuiopasdfghjklzxcvbnm"

for a in alphas:
    mrxn = mrxn.replace(a, "")
    mrxn = mrxn.replace(a.upper(), "")

    for r in mrxn:
        if not ongoing_count:
            ongoing_count.append(r)
        else:
            comp_char = ongoing_count[-1]

            if ord(comp_char) - ord(r) == 32 or ord(comp_char) - ord(r) == -32:
                ongoing_count.pop()
            else:
                ongoing_count.append(r)

    shortest = min(shortest, len(ongoing_count))
    mrxn = rxn
    ongoing_count = []

print(shortest)

