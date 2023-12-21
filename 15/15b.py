from collections import defaultdict
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    blocks = file.read().split(",")

M = defaultdict(list)

for block in blocks:
    eqa = "=" in block
    val = 0
    if eqa:
        kee, num = block.split("=")
    else:
        kee = block[:-1]

    for ch in kee:
        val += ord(ch)
        val *= 17
        val %= 256

    mat = [i for i, (k, _) in enumerate(M[val]) if k == kee]
    if eqa:
        if mat:
            M[val][mat[0]] = (kee, int(num))
        else:
            M[val].append((kee, int(num)))
    else:
        if mat:
            M[val].pop(mat[0])


zum = []
for k, v in M.items():
    for i, (_, foc) in enumerate(v):
        zum.append((k + 1) * (i + 1) * foc)

print(zum)
print(sum(zum))
