import numpy as np

def read_data(path):
    with open(path) as f:
        lines = f.read().splitlines()
    return np.array([np.fromstring(line, dtype=int, sep=' ') for line in lines], dtype=object)

def is_safe_sequence(diffs):
    return np.all((1 <= diffs) & (diffs <= 3)) or np.all((-3 <= diffs) & (diffs <= -1))

def part_one(rep):
    diffs = np.diff(rep)
    return int(is_safe_sequence(diffs))

def part_two(rep):
    if part_one(rep):
        return 1
    return int(any(part_one(np.delete(rep, i)) for i in range(len(rep))))

def main():
    data = read_data("day2/day2.txt")
    partone =  sum(part_one(x) for x in data)
    parttwo = sum(part_two(x) for x in data)
    print(f"Part one: {partone}\nPart two: {parttwo}")

if __name__ == "__main__":
    main()
