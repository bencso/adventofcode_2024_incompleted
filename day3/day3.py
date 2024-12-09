import regex

def read_data(input_file_dir):
    with open(input_file_dir, 'r') as file:
        return file.read()

def part_one(mem):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    total = sum(int(x) * int(y) for x, y in regex.findall(pattern, mem))
    return total

def part_two(mem):
    return [e.split("don't()")[0] for e in mem.split("do()")]

def sum_part_two(mem):
    filtered_mem = part_two(mem)
    joined_mem = ' '.join(filtered_mem)
    return part_one(joined_mem)

def main():
    data = read_data('day3/day3.txt')
    part_one_result = part_one(data)
    part_two_result = sum_part_two(data)
    print(f"Part one: {part_one_result}\nPart two: {part_two_result}")

if __name__ == '__main__':
    main()
