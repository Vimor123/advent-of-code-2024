input_file = open("input.txt")

s = 0

for line in input_file:
    report = [int(x) for x in line.split()]
    if len(report) > 2:
        safe = True
        ascending = False
        if report[1] > report[0]:
            ascending = True
        elif report[1] < report[0]:
            ascending = False
        else:
            safe = False

        for i in range(1, len(report)):
            distance = abs(report[i] - report[i - 1])
            if distance < 1 or distance > 3:
                safe = False
            if ascending and report[i] < report[i - 1]:
                safe = False
            if not ascending and report[i] > report[i - 1]:
                safe = False

        if safe:
            s += 1

    elif abs(report[0] - report[1]) <= 3 and report[0] != report[1]:
        s += 1

input_file.close()

print(s)
