import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    blocks = file.read().split("\n\n")

k = []

for block in blocks:
    lines = block.split("\n")
    cols = [
        "".join(lines[y][x] for y in range(len(lines))) for x in range(len(lines[0]))
    ]

36474

print(k)
print(sum(k))
