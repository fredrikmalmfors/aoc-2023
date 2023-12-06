from curses.ascii import isdigit
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

zum = []

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
                    # print(dac)
                    if (not dac.isdigit()) and (dac != "."):
                        # print("VALID", dac)
                        valid = True
                        break
            if valid:
                print(nums)
                zum.append(int(nums))

            nums = ""
            roll = False

print("---------------")
print(sum(zum))

# 537710 too low?
# 538664 too low?
