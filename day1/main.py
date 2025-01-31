from functools import reduce

# Read the input file
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split("\n")

# Process the data
left_list = []
right_list = []
for line in data:
    left_num, right_num = line.strip().split()
    left_list.append(left_num)
    right_list.append(right_num)

distances = []


def calculate_distance(sorted_left, sorted_right):
    results = []
    for left_val, right_val in zip(sorted_left, sorted_right):
        results.append(abs(left_val - right_val))  # Use abs() for distance
    final_distance = reduce(lambda a, b: a + b, results)
    # print("FInal", final_distance)
    distances.append(final_distance)


def get_item(left_arr, right_arr):
    for i, value in enumerate(left_arr):
        left_val = sorted(map(int, value))  # Combine map and sort
        right_val = sorted(map(int, right_arr[i]))
        calculate_distance(left_val, right_val)


get_item(left_list, right_list)
res = reduce(lambda a, b: a + b, distances)

print(res)
