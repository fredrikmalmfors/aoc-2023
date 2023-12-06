from collections import defaultdict
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

zum = []

for ll in lines:
    a, b = ll.split(": ")
    b, c = b.split(" | ")
    b = [x for x in b.split(" ") if x]
    c = [x for x in c.split(" ") if x]

    haha = len(set.intersection(set(b), set(c)))
    if haha > 0:
        zum.append(2 ** (haha - 1))

print(sum(zum))
