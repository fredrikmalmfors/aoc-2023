from collections import defaultdict
import numpy as np

# Time, Dist
# data = [(7, 9), (15, 40), (30, 200)] # Sample
data = [(38, 241), (94, 1549), (79, 1074), (70, 1091)]
zum = []
for ttime, dist_record in data:
    ka = 0
    for hmsec in range(0, ttime):
        dist = hmsec * (ttime - hmsec)
        if dist > dist_record:
            ka += 1
    zum.append(ka)
print(np.prod(zum))
