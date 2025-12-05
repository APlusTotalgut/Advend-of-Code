with open('./data/ingredient_list.txt') as file:
    ranges = []
    ids = []
    for line in file:
        if '-' in line:
            start, end = line.split('-')
            ranges.append([int(start), int(end)])
        elif line.strip() != '':
            ids.append(int(line.strip()))

    fresh_ids_count = 0
    fresh_ids = []
    for fresh_id in ids:
        for start, end in ranges:
            if start <= fresh_id <= end:
                if not fresh_id in fresh_ids:
                    fresh_ids_count += 1
                    fresh_ids.append(fresh_id)
    print(fresh_ids_count)
