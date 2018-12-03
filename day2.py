ids = [str(x) for x in open("./input/day2-input.txt").readlines()]
alphas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Part 1

twos = 0 
threes = 0
has_two = False
has_three = False

for i in ids:
    for j in alphas:
        if i.count(j) == 3 and not has_three:
            threes += 1
            has_three = True
        elif i.count(j) == 2 and not has_two:
            twos += 1
            has_two = True
    has_three = False
    has_two = False

print(twos * threes)

# Part 2

different_characters = 0

for i in ids:
    for j in ids:
        different_characters = 0
        for r in range(len(i)):
            if i[r] != j[r]:
                different_characters += 1
        if different_characters == 1:
            for r in range(len(i)):
                if i[r] == j[r]:
                    print(i[r], end='')
