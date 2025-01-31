
with open("input.txt", "r", encoding="utf-8") as file:
    data = file.read().strip().split("\n")

# Convert input to a list of lists
newData = [list(map(int, line.split())) for line in data]

safe_reports = []
unsafe_reports = []
nein_reports = []

for report in newData:
    is_safe = True  # Assume the report is safe until proven otherwise

    if report == sorted(report):  # Ascending order
        print("Ascending")
        for j in range(len(report) - 1):
            if abs(report[j] - report[j+1]) > 3:
                unsafe_reports.append(report)
                is_safe = False  # Mark as unsafe
                break  # Stop checking further

    elif report == sorted(report, reverse=True):  # Descending order
        print("Descending")
        for j in range(len(report) - 1):
            if abs(report[j] - report[j+1]) > 2:
                unsafe_reports.append(report)
                is_safe = False  # Mark as unsafe
                break  # Stop checking further

    else:  # Neither ascending nor descending
        print("Neither")
        unsafe_reports.append(report)
        nein_reports.append(report)
        is_safe = False

    if is_safe:  # If it survived the checks, add it to safe_reports
        safe_reports.append(report)

print(f"Safe {len(safe_reports)}, Unsafe {len(unsafe_reports)}")
print(f"Nein {len(nein_reports)}")
