from copy import deepcopy
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    blocks = file.read().split("\n\n")

k = []

for block in blocks:
    print("---------------")
    b_lines = block.split("\n")
    b_cols = [
        "".join(b_lines[y][x] for y in range(len(b_lines)))
        for x in range(len(b_lines[0]))
    ]

    kloc = []

    bad = None

    for tt, view in enumerate([b_lines, b_cols]):
        for step in range(len(view)):
            i = 0
            mat = []
            while True:
                if step - i < 0 or step + 1 + i >= len(view):
                    break

                if view[step - i] == view[step + 1 + i]:
                    mat.append(True)
                    i += 1
                else:
                    mat.append(False)
                    break

            if mat and all(mat):
                ha = step + 1
                if not tt:
                    ha *= 100
                print("bad ->", step, mat, tt, ha)
                bad = ha
                break

    for yy in range(len(b_lines)):
        for xx in range(len(b_cols)):
            lines = deepcopy(b_lines)
            cols = deepcopy(b_cols)

            lines[yy] = (
                lines[yy][:xx]
                + ("#" if lines[yy][xx] == "." else ".")
                + lines[yy][xx + 1 :]
            )
            cols[xx] = (
                cols[xx][:yy]
                + ("#" if cols[xx][yy] == "." else ".")
                + cols[xx][yy + 1 :]
            )

            for tt, view in enumerate([lines, cols]):
                for step in range(len(view)):
                    i = 0
                    mat = []
                    while True:
                        if step - i < 0 or step + 1 + i >= len(view):
                            break

                        if view[step - i] == view[step + 1 + i]:
                            mat.append(True)
                            i += 1
                        else:
                            mat.append(False)
                            break

                    if mat and all(mat):
                        ha = step + 1
                        if not tt:
                            ha *= 100
                        print("YES", (yy, xx), step, mat, tt, ha)
                        kloc.append(ha)

    hoic = set(kloc) - set([bad])
    print(set(kloc), bad)
    if len(hoic) == 1:
        k.append(list(hoic)[0])
    elif len(set(kloc)) == 1:
        assert False
        k.append(list(kloc)[0])
    else:
        assert False

print(sum(k))

# 29989 too low
