import sys
from copy import copy

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

part2 = True

results = []
for ii, ll in enumerate(lines):
    a, b = ll.split()
    if part2:
        a = "?".join([a] * 5)
        b = ",".join([b] * 5)

    b = [int(x) for x in b.split(",")]
    MEM = {}  # Very important

    def trav(rest: str, active: bool = False, score: list[int] = []):
        cool_hash = (rest, active, str(score))
        if cool_hash in MEM:
            return MEM[cool_hash]

        res = 0

        if rest == "":
            return 1 if score == b else 0

        if len(score) > len(b):
            return 0

        if score:
            for i in range(len(score)):
                if score[i] > b[i]:
                    return 0

        if len(score) >= 2:
            for i in range(len(score) - 1):
                if score[i] != b[i]:
                    return 0

        n_score = copy(score)

        if rest[0] in ["?", "#"]:
            l_score = copy(n_score)
            if active:
                l_score[-1] += 1
            else:
                l_score.append(1)
            res += trav(rest[1:], True, l_score)

        if rest[0] in ["?", "."]:
            res += trav(rest[1:], False, n_score)

        # Memoize
        MEM[cool_hash] = res

        return res

    ans = trav(a)
    results.append(ans)

print("-->", sum(results))
# 3415570893842
