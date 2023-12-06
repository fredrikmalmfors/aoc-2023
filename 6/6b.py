from collections import defaultdict
from math import floor
import numpy as np
import math
import cmath

# ttime, dist_record = 71530, 940200  # Sample
ttime, dist_record = 38947970, 241154910741091  # Real

d = (ttime**2) - (4 * dist_record)
sol1 = (-ttime - cmath.sqrt(d)) / 2
sol2 = (-ttime + cmath.sqrt(d)) / 2
print(sol1, sol2)
print(floor(abs(sol1.real)) - math.ceil(abs(sol2.real)) + 1)
