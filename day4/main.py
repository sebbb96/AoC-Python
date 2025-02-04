with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split("\n")


word_search = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]
directions = [
    (1, 0),  # Down
    (-1, 0),  # Up
    (0, 1),  # Right
    (0, -1),  # Left
    (1, 1),  # Down-Right
    (1, -1),  # Down-Left
    (-1, 1),  # Up-Right
    (-1, -1),  # Up-Left
]
list_grid = [list(row) for row in data]

# Part 2


def count_mas_in_x(grid):
    """Part 2"""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    target_mas = "MAS"
    target_sam = "SAM"
    count = 0  # Directions for the two pairs of diagonals forming an "X"

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "A":  # The center of the "X"
                left_dia = ""
                right_dia = ""
                # print(grid[i][j])
                if i - 1 < 0 or i + 1 >= rows or j - 1 < 0 or j + 1 >= cols:
                    continue

                left_dia = "".join(
                    [grid[i - 1][j - 1], grid[i][j], grid[i + 1][j + 1]])
                right_dia = "".join(
                    [grid[i - 1][j + 1], grid[i][j], grid[i + 1][j - 1]]
                )
                if (left_dia in (target_mas, target_sam)) and (
                    right_dia in (target_mas, target_sam)
                ):
                    count += 1
    return count

# Part 1


def count_xmas_occurrences(grid):
    """Part 1"""
    rows = len(grid)
    cols = len(grid[0])
    target = "XMAS"
    count = 0

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                sequence = ""
                x, y = i, j
                for _ in range(len(target)):
                    if 0 <= x < rows and 0 <= y < cols:
                        sequence += grid[x][y]
                        x += dx
                        y += dy
                    else:
                        break
                if sequence == target:
                    count += 1
    return count


print(count_mas_in_x(list_grid))
