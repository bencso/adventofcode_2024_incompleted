from collections import defaultdict

def read_data(path):
    with open(path, 'r') as file:
        return file.read()

def part_one(data):
    def parse_data(data):
        rules = []
        updates = []
        for line in data.split("\n"):
            if "|" in line:
                a, b = line.split("|")
                rules.append((int(a), int(b)))
            elif "," in line:
                updates.append(list(map(int, line.split(","))))
        return rules, updates

    def check_rules(rules, update):
        checked_rules = {num: i for i, num in enumerate(update)}
        for a, b in rules:
            if a in checked_rules and b in checked_rules and not checked_rules[a] < checked_rules[b]:
                return False, 0
        return True, update[len(update) // 2]
    rules, updates = parse_data(data)
    count = 0
    for update in updates:
        good, mid = check_rules(rules, update)
        if good:
            count += mid
    return count

def main():
    data = read_data('day5/day5.txt')
    print(f"Part one: {part_one(data)}")

if __name__ == "__main__":
    main()