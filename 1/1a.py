import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    lines = file.read().splitlines()

DAS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print("\n------------------\n")
val = 0
for ll in lines:
    koi = []
    for i in range(len(ll)):
        for ii, das in enumerate(DAS):
            if ll[i:].startswith(das):
                koi.append(ii)
            elif ll[i].isdigit():
                koi.append(int(ll[i]))
                break
    print(koi)
    val += 10 * koi[0] + koi[-1]

print(val)
