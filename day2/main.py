
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split("\n")

# Convert input to a list of lists
newData = [list(map(int, line.split())) for line in data]
test_data = [
    [7, 6, 4, 2, 1],  # Safe ✅
    [1, 2, 7, 8, 9],  # Unsafe ❌
    [9, 7, 6, 2, 1],  # Unsafe ❌
    [1, 3, 2, 4, 5],  # Unsafe ❌
    [8, 6, 4, 4, 1],  # Unsafe ❌
    [1, 3, 6, 7, 9],   # Safe ✅
    # [66, 67, 70, 73, 74, 76, 78, 80],
    # [2, 2, 2, 2, 2, 2]

]


def is_safe_report(report):
    """Check if a report is safe using the original rules."""
    trend = None  # 'up' for increasing, 'down' for decreasing

    for j in range(len(report) - 1):
        diff = report[j + 1] - report[j]

        if diff == 0:
            return False

        if trend is None:
            trend = 'up' if diff > 0 else 'down'

        elif (trend == 'up' and diff < 0) or (trend == 'down' and diff > 0):
            return False

        if abs(diff) > 3:
            return False

    return True


safe_reports = []
unsafe_reports = []

for report in newData:
    if is_safe_report(report):
        safe_reports.append(report)
    else:
        found_fix = False
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]  # Remove index `i`
            if is_safe_report(modified_report):
                safe_reports.append(report)
                found_fix = True
                break
        if not found_fix:
            unsafe_reports.append(report)

# ✅ Print results
print(f"Safe {len(safe_reports)}, Unsafe {len(unsafe_reports)}")
print(f"Safe Reports: {safe_reports}")
print(f"Unsafe Reports: {unsafe_reports}")
print(f"Safe {len(safe_reports)}, Unsafe {len(unsafe_reports)}")
