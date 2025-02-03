from collections import Counter
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split("\n")

# Process the data into two separate lists
left_list = []
right_list = []
for line in data:
    left_num, right_num = map(int, line.strip().split())
    left_list.append(left_num)
    right_list.append(right_num)

left_list.sort()
right_list.sort()

# Compute distances
total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
right_counts = Counter(right_list)

SIMILARITY_SCORE = 0
for num in left_list:
    occurrences = right_counts.get(num, 0)
    SIMILARITY_SCORE += num * occurrences

print("Total Distance:", total_distance)
print("Similarity Score:", SIMILARITY_SCORE)
