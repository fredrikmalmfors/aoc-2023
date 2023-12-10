dimport sys
from collections import defaultdict, Counter
import numpy as np
import math

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()


def rec(data: list[int]) -> int:
    if all(x == 0 for x in data):
        return 0
    diff = [data[i + 1] - data[i] for i in range(len(data) - 1)]
    return data[0] - rec(diff)


zum = []
for line in lines:
    a = [int(x) for x in line.split()]
    res = rec(a)
    print(res)
    zum.append(res)

print("Answer:")
print(sum(zum))
