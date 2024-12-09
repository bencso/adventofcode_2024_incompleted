def read_data(path):
    with open(path, 'r') as file:
        data = file.read().split('\n')
    return [p.split("   ") for p in data]

def part_one(left, right):
    left.sort(key=int)
    right.sort(key=int)
    result = 0
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        result += abs(int(left[left_index]) - int(right[right_index]))
        left_index += 1
        right_index += 1
    return result

def part_two(left, right):
    score = 0
    for num in left:
        count = right.count(num)
        score += int(num) * count
    return score

def main():
    row = read_data('day1/day1.txt')
    left = [element[0] for element in row]
    right = [element[1] for element in row]
    partone = part_one(left, right)
    parttwo = part_two(left, right)

    print(f"Part one: {partone}\nPart two: {parttwo}")
    
if __name__ == '__main__':
    main()