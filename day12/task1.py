input_file = open("input.txt")

plot_map = []
region_map = []
region_id = -1
same_area_ids = {}
for line in input_file:
    row = list(line.strip())
    plot_map.append(row)
    region_row = []
    for i in range(len(row)):
        current_plot = row[i]
        connected = False

        if len(plot_map) > 1:
            if plot_map[-2][i] == current_plot:
                region_row.append(region_map[-1][i])
                connected = True

        if i > 0:
            if row[i - 1] == current_plot:
                if not connected:
                    region_row.append(region_row[i - 1])
                    connected = True
                elif region_row[i] != region_row[i - 1]:
                    same_area_ids[region_row[i]].update(same_area_ids[region_row[i - 1]])
                    same_area_ids[region_row[i - 1]].update(same_area_ids[region_row[i]])
                    for area_id in same_area_ids[region_row[i]]:
                        same_area_ids[area_id].update(same_area_ids[region_row[i]])

        if not connected:
            region_id += 1
            region_row.append(region_id)
            same_area_ids[region_id] = {region_id}
    
    region_map.append(region_row)

input_file.close()

final_region_map = []
for region_row in region_map:
    final_region_row = []
    for region_id in region_row:
        final_region_row.append(min(same_area_ids[region_id]))
    final_region_map.append(final_region_row)

regions = {}
for i in range(len(final_region_map)):
    for j in range(len(final_region_map[i])):
        borders = 0
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for direction in directions:
            if i + direction[0] in range(len(final_region_map)) and j + direction[1] in range(len(final_region_map[i + direction[0]])):
                if final_region_map[i + direction[0]][j + direction[1]] != final_region_map[i][j]:
                    borders += 1
            else:
                borders += 1
        if final_region_map[i][j] not in regions:
            regions[final_region_map[i][j]] = {"area" : 1, "perimeter" : borders}
        else:
            regions[final_region_map[i][j]]["area"] += 1
            regions[final_region_map[i][j]]["perimeter"] += borders

s = 0
for region, stats in regions.items():
    s += stats["area"] * stats["perimeter"]
print(s)
