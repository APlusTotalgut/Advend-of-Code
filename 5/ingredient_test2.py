with open('./data/ingredient_list.txt') as file:
    ranges = []
    total = 0
    for line in file:
        if '-' in line:
            start, end = line.split('-')
            ranges.append([int(start),int(end.strip())])
    for index, (start, end) in enumerate(ranges):
        for index_iterate, (start_iterate, end_iterate) in enumerate(ranges):
            if index_iterate != index:
                if start <= start_iterate <= end:
                    ranges[index_iterate][0] = end + 1
    print(ranges)
    for index, (start, end) in enumerate(ranges):
        id_range = end - start
        if id_range < 0:
            print(f"help at index {index}")
            continue
        total += id_range + 1

    print(total)
