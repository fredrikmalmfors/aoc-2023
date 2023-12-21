from collections import deque
import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
CHARS = "|-/\\."
ACTION = "01011010232332321111"
VISITED = set()
BEAMS = deque([((0, -1), 0)])
while BEAMS:
    curr = BEAMS.popleft()
    if curr in VISITED:
        continue
    VISITED.add(curr)
    (y, x), aim = curr

    # Step
    dy, dx = DIRS[aim]
    ny, nx = y + dy, x + dx

    if not ((0 <= ny < len(lines)) and (0 <= nx < len(lines[0]))):
        continue

    npos = (ny, nx)
    left, same, right = [(npos, (aim + x) % 4) for x in (-1, 0, 1)]

    moves = [
        [left, right],
        [same],
        [left],
        [right],
        [same],
    ]

    BEAMS += moves[int(ACTION[4 * CHARS.index(lines[ny][nx]) + aim])]

print(len(set(pos for pos, _ in VISITED)) - 1)
