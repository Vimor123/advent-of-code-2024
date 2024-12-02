input_file = open("input.txt")

s = 0

def is_report_safe(report):
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

        return safe

    elif len(report) == 2:
        if abs(report[0] - report[1]) <= 3 and report[0] != report[1]:
            return True
        else:
            return False

    else:
        return True

for line in input_file:
    report = [int(x) for x in line.split()]
    if len(report) > 2:
        if is_report_safe(report):
            s += 1
        else:
            safe = False
            for i in range(len(report)):
                report_copy = report.copy()
                report_copy.pop(i)
                if is_report_safe(report_copy):
                    safe = True
            if safe:
                s += 1
    else:
        s += 1

input_file.close()

print(s)
