def read_data(path):
    with open(path, 'r') as file:
        return file.read().splitlines()

def part_one(data):
    keyword = "XMAS"
    
    def count_keyword(data, row, col, row_step, col_step):
        for index, char in enumerate(keyword):
            _row = row + index * row_step
            _col = col + index * col_step
            if not (0 <= _row < len(data) and 0 <= _col < len(data[0])):
                return False
            if data[_row][_col] != char:
                return False
        return True

    def find(data):
        directions = [(row_step, col_step) for row_step in range(-1, 2) for col_step in range(-1, 2) if row_step != 0 or col_step != 0]
        count = 0
        
        for row in range(len(data)):
            for col in range(len(data[0])):
                for row_step, col_step in directions:
                    if count_keyword(data, row, col, row_step, col_step):
                        count += 1
        return count
   
    
    return find(data)

def part_two(data):
    def find(data, row, col):
        if not 1 <= row < len(data) - 1 or not 1 <= col < len(data[0]) - 1:
            return False
        if data[row][col] != "A":
            return False

        diag1 = f"{data[row-1][col-1]}{data[row+1][col+1]}"
        diag2 = f"{data[row-1][col+1]}{data[row+1][col-1]}"

        return diag1 in ["MS", "SM"] and diag2 in ["MS", "SM"]

    def count(data):
        count = 0
        for row in range(len(data)):
            for col in range(len(data[0])):
                if find(data, row, col):
                    count += 1
        return count

    return count(data)
    
def main():
    data = read_data('day4/day4.txt')
    print(f"Part one: {part_one(data)}")
    print(f"Part two: {part_two(data)}")

if __name__ == "__main__":
    main()
