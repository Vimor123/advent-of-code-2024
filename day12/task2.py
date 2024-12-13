input_file = open("input.txt")

def find_no_of_edges(region_map, region_id):
    edges = []
    for i in range(len(region_map)):
        for j in range(len(region_map[i])):
            if region_map[i][j] == region_id:
                borders = []
                directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
                for direction in directions:
                    if i + direction[0] in range(len(region_map)) and j + direction[1] in range(len(region_map[i + direction[0]])):
                        if region_map[i + direction[0]][j + direction[1]] != region_id:
                            if direction[0] == 0:
                                borders.append(("v", (j, j + direction[1])))
                            else:
                                borders.append(("h", (i, i + direction[0])))
                    else:
                        if direction[0] == 0:
                            borders.append(("v", (j, j + direction[1])))
                        else:
                            borders.append(("h", (i, i + direction[0])))

                for border in borders:
                    if border in edges:
                        pass
                    else:
                        edges.append(border)

    no_of_edges = 0
    for edge in edges:
        if edge[0] == "h":
            i = edge[1][0]
            i2 = edge[1][1]
            continuity = False
            for j in range(len(region_map[0])):
                if region_map[i][j] == region_id:
                    if i2 in range(len(region_map)):
                        if region_map[i2][j] != region_id:
                            if continuity:
                                pass
                            else:
                                continuity = True
                                no_of_edges += 1
                        else:
                            continuity = False
                    else:
                        if continuity:
                            pass
                        else:
                            continuity = True
                            no_of_edges += 1
                else:
                    continuity = False
        else:
            j = edge[1][0]
            j2 = edge[1][1]
            continuity = False
            for i in range(len(region_map)):
                if region_map[i][j] == region_id:
                    if j2 in range(len(region_map[0])):
                        if region_map[i][j2] != region_id:
                            if continuity:
                                pass
                            else:
                                continuity = True
                                no_of_edges += 1
                        else:
                            continuity = False
                    else:
                        if continuity:
                            pass
                        else:
                            continuity = True
                            no_of_edges += 1
                else:
                    continuity = False
    return no_of_edges

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
        if final_region_map[i][j] not in regions:
            edges = find_no_of_edges(final_region_map, final_region_map[i][j])
            regions[final_region_map[i][j]] = {"area" : 1, "edges" : edges}
        else:
            regions[final_region_map[i][j]]["area"] += 1

s = 0
for region, stats in regions.items():
    s += stats["area"] * stats["edges"]
print(s)
