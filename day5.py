import re

rxn = [str(x) for x in open("./input/day5-input.txt").readlines()][0].strip('\n')

# Part 1

mrxn = rxn

while True:
    reacted = False
    for i in range(len(mrxn) - 1):
        if not mrxn[i] == mrxn[i + 1]: # do nothing if they're exactly the same
            if mrxn[i].lower() == mrxn[i + 1].lower():
                reacted = True
                mrxn = mrxn[0:i] + mrxn[i + 2:len(mrxn)] # remove both indices i and i + 1
                break
    if not reacted:
        print(len(mrxn))
        break


# Part 2

shortest = len(rxn)
alphas = "qwertyuiopasdfhjklzxcvbnm"

for a in alphas:
    mrxn = rxn
    while True:
        removed = False
        for i in range(len(mrxn) - 1):
            if mrxn[i].lower() == a:
                mrxn = mrxn[0:i] + mrxn[i + 1:len(mrxn)]
                removed = True
                break
        if not removed:
            break

    while True:
        reacted = False
        for j in range(len(mrxn) - 1):
            if not mrxn[j] == mrxn[j + 1]: # do nothing if they're exactly the same
                if mrxn[j].lower() == mrxn[j + 1].lower():
                    reacted = True
                    mrxn = mrxn[0:j] + mrxn[j + 2:len(mrxn)] # remove both indices i and i + 1
                    break
        if not reacted:
            shortest = min(len(mrxn, shortest))
            break
print(shortest)