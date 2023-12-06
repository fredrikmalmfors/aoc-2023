import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

KALA = {"red": 12, "green": 13, "blue": 14}
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

    print(maxi)

    possible = True

    for k in KALA.keys():
        if KALA[k] < maxi[k]:
            possible = False

    if not possible:
        continue

    koi.append(int(a.strip().split(" ")[-1]))

print(koi)
print(sum(koi))
