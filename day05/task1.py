input_file = open("input.txt")

def is_update_correctly_ordered(rules, update):
    for i in range(len(update)):
        current_element = update[i]
        for j in range(0, i):
            if update[j] in rules[current_element]["before"]:
                return False
        for k in range(i + 1, len(update)):
            if update[k] in rules[current_element]["after"]:
                return False
    return True


rules = {}
updates = []
reading_rules = True
for line in input_file:
    if reading_rules:
        if line.strip() == "":
            reading_rules = False
        else:
            element1, element2 = [int(x) for x in line.strip().split("|")]
            if element1 in rules:
                rules[element1]["before"].append(element2)
            else:
                rules[element1] = {"before" : [element2], "after" : []}
            if element2 in rules:
                rules[element2]["after"].append(element1)
            else:
                rules[element2] = {"before" : [], "after" : [element1]}
    else:
        updates.append([int(x) for x in line.strip().split(",")]) 

input_file.close()

s = 0
for update in updates:
    if is_update_correctly_ordered(rules, update):
        s += update[len(update) // 2]

print(s)
