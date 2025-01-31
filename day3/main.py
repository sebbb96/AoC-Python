import re
from functools import reduce
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip()


PATTERN = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

matches = re.findall(PATTERN, data)


func_calls = [[int(a), int(b)] for a, b in re.findall(PATTERN, data)]

# print(func_calls)
results = []
for arr in func_calls:
    results.append(arr[0] * arr[1])


res = reduce(lambda a, b: a + b, results)

print(res)
PATTERN_FOR_SKIP = r"(do\(\))|(don't\(\))|mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

# Flag to determine whether to process mul()
PROCESS_MUL = False
mul_calls = []

for match in re.finditer(PATTERN_FOR_SKIP, data):
    if match.group(1):  # Found 'do()'
        PROCESS_MUL = True
    elif match.group(2):  # Found 'don't()'
        PROCESS_MUL = False
    elif PROCESS_MUL and match.group(3) and match.group(4):
        mul_calls.append([int(match.group(3)), int(match.group(4))])
mul_calls_calc = []
for call in mul_calls:
    mul_calls_calc.append(call[0] * call[1])
res_skip = reduce(lambda a, b: a + b, mul_calls_calc)


print(res_skip)
