import sys
from collections import defaultdict, Counter
import numpy as np

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

ORD = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def hoj(cc: dict):
    cc = dict(Counter(cc))
    vs = set(cc.values())
    if len(cc) == 1:
        return 1
    if len(cc) == 2:
        if vs == set([4, 1]):
            return 2
        if vs == set([3, 2]):
            return 3
        assert False
    if len(cc) == 3:
        if vs == set([3, 1]):
            return 4
        if vs == set([2, 1]):
            return 5
        assert False
    if len(cc) == 4:
        return 6
    if len(cc) == 5:
        return 7

    assert False


KVAL = {}


for ll in lines:
    a, b = ll.split()
    KVAL[a] = int(b)

data = list(KVAL.keys())

ok = list(
    sorted(
        data,
        key=lambda x: hoj(x) * 10000000000
        + ORD.index(x[0]) * 100000000
        + ORD.index(x[1]) * 1000000
        + ORD.index(x[2]) * 10000
        + ORD.index(x[3]) * 100
        + ORD.index(x[4]),
    )
)
ok.reverse()
res = [KVAL[x] * (i + 1) for i, x in enumerate(ok)]
for kk in ok:
    print(kk, KVAL[kk])
print(res)
print(sum(res))
