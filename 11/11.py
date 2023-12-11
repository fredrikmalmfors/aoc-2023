import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

coords = set()
empty_rows = set()
for y in range(len(lines)):
    if "#" not in lines[y]:
        empty_rows.add(y)
        continue
    for x in range(len(lines[0])):
        if lines[y][x] == "#":
            coords.add((y, x))

empty_cols = set()
for x in range(len(lines[0])):
    if "#" not in [line[x] for line in lines]:
        empty_cols.add(x)

factor = 1_000_000  # 2 for part 1

tot_dist = 0
for a in coords:
    for b in coords:
        if a == b:
            continue
        tot_dist += (
            abs(a[0] - b[0])
            + abs(a[1] - b[1])
            + len([y for y in empty_rows if min(a[0], b[0]) < y < max(a[0], b[0])])
            * (factor - 1)
            + len([x for x in empty_cols if min(a[1], b[1]) < x < max(a[1], b[1])])
            * (factor - 1)
        )

print(tot_dist // 2)
