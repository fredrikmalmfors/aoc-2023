from collections import defaultdict
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

CC = defaultdict(list)

for y, ll in enumerate(lines):
    roll = False
    nums = ""
    for x, ch in enumerate(ll):
        if ch.isdigit():
            roll = True
            nums += ch
        if (roll and (not ch.isdigit())) or (
            roll and ch.isdigit() and x == len(ll) - 1
        ):
            # Check adjecent
            # print("\n\nROLL---------\n")
            valid = False
            if roll and ch.isdigit() and x == len(ll) - 1:
                _x = x + 1
            else:
                _x = x
            # print(y, x - len(nums), x, nums)
            for yy in range(y - 1, y + 2):
                for xx in range(_x - len(nums) - 1, _x + 1):
                    if xx < 0 or len(lines[0]) <= xx:
                        continue
                    if yy < 0 or len(lines[0]) <= yy:
                        continue
                    if yy == y and xx in range(_x - len(nums), _x):
                        continue

                    dac = lines[yy][xx]
                    if dac == "*":
                        CC[(yy, xx)].append(int(nums))

            nums = ""
            roll = False

# print("---------------")
# print(CC)
# for k, v in CC.items():
#     if len(v) != 2:
#         continue
#     print(k, v[0] * v[1])

ans = sum(v[0] * v[1] for v in CC.values() if len(v) == 2)
print(ans)

# 537710 too low?
# 538664 too low?
