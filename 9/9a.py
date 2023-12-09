import sys
from collections import defaultdict, Counter
import numpy as np

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()


def rec(data: list[int]) -> int:
    if all(x == 0 for x in data):
        return 0
    diff = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    return rec(diff) + data[-1]


zum = []
for line in lines:
    a = [int(x) for x in line.split()]
    res = rec(a)
    zum.append(res)

print("Answer:")
print(sum(zum))
