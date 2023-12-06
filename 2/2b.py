import sys
import numpy as np

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

koi = []

for ll in lines:
    maxi = {"red": 0, "green": 0, "blue": 0}

    a, b = ll.split(":")
    bl = b.split(";")
    bl2 = [x.split(",") for x in bl]
    for show in bl2:
        for piece in show:
            am, color = piece.strip().split(" ")
            am = int(am)
            maxi[color] = max(maxi[color], am)

    hehe = np.prod(list(maxi.values()))
    koi.append(hehe)

print(sum(koi))
