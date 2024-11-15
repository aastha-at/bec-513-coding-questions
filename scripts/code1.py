import sys

with open("../data/to_select.tsv", "r") as f:
    patterns={line.strip() for line in f if line.strip()}

for line in sys.stdin:
    line=line.strip()
    if any(pattern in line for pattern in patterns):
        print(line)

