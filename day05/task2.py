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


def order_update_correctly(rules, update):
    new_update = update.copy()
    level = 0
    while level < len(new_update):
        current_element = new_update[level]
        level_passed = True
        for j in range(level + 1, len(update)):
            if new_update[j] in rules[current_element]["after"]:
                element = new_update.pop(j)
                new_update.insert(level, element)
                level = 0
                level_passed = False
                break

        if level_passed:
            level += 1

    return new_update


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
    if not is_update_correctly_ordered(rules, update):
        new_order = order_update_correctly(rules, update)
        s += new_order[len(new_order) // 2]

print(s)
