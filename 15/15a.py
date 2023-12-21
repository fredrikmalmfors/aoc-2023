import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    blocks = file.read().split(",")

zum = []
for block in blocks:
    val = 0
    for ch in block:
        val += ord(ch)
        val *= 17
        val %= 256
    print(val)
    zum.append(val)

print(sum(zum))
