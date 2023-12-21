from collections import deque
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

ROLL = deque()
STILL = set()
BL = set()

for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "#":
            BL.add((y, x))
        elif lines[y][x] == "O":
            STILL.add((y, x))

cc = 0
hiz = []
while True:
    for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ROLL = deque(sorted(STILL, key=lambda hej: hej[0] * -dy + hej[1] * -dx))
        STILL = set()

        while ROLL:
            y, x = ROLL.popleft()
            if (
                (dy == -1 and y == 0)
                or (dx == -1 and x == 0)
                or (dy == 1 and y == len(lines) - 1)
                or (dx == 1 and x == len(lines[0]) - 1)
                or ((y + dy, x + dx) in STILL)
                or ((y + dy, x + dx) in BL)
            ):
                STILL.add((y, x))
            else:
                ROLL.append((y + dy, x + dx))

        if (dy, dx) == (0, 1):
            # print board
            # for y in range(len(lines)):
            #     ll = ""
            #     for x in range(len(lines[0])):
            #         if (y, x) in BL:
            #             ll += "#"
            #         elif (y, x) in STILL:
            #             ll += "O"
            #         else:
            #             ll += "."
            #     print(ll)
            # print("")

            cc += 1
            points = sum(len(lines) - y for y, _ in STILL)
            hiz.append(points)
            print(cc, "|", points)

            # Find periodicity
            if len(hiz) > 10:
                step = 2
                while (1 + (2 * step)) < len(hiz):
                    if hiz[-1] == hiz[-(1 + step)] == hiz[-(1 + (2 * step))]:
                        print("YAA", step, cc)
                        koik = (1000000000 - cc) // step
                        ans = koik * step + cc
                        offset = 1000000000 - ans
                        look = cc - step + offset
                        print("-->", hiz[look - 1])
                        sys.exit()
                    step += 1

            if cc == 2000000:
                sys.exit()
