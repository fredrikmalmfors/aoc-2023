import sys

filename = "input" if len(sys.argv) > 1 else "sample"

with open(f"{filename}.txt") as file:
    blocks = file.read().splitlines()
