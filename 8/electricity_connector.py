def get_3d_distance(p, q):
    return (abs(p[0] - q[0]) ** 2 + abs(p[1] - q[1]) ** 2 + abs(p[2] - q[2]) ** 2) ** 0.5

with open('./data_small.txt') as data:
    data = data.read().split('\n')
    sdata = []
    for d in data:
        sdata.append([int(d) for d in d.split(',')])

connections = {}

for pidx, p in enumerate(sdata):
    lowest = []  # 0 => point itself ; 1 => distance
    for qidx, q in enumerate(sdata):
        if qidx == pidx:
            continue
        distance = get_3d_distance(p, q)
        if not lowest or distance < lowest[1]:
            lowest = [q, distance]
    connections[tuple(p)] = lowest

circuits = {}
for cp, cq in connections.items():
    for p2, q2 in connections.items():
        if cp != p2:
            if list(cp) == q2[0]:
                if cp not in circuits:
                    circuits[cp] = []
                circuits[cp].append(p2)

def find_pair(t):
    return circuits[t] if t in circuits else False
def find_and_check_all(pair, all_pairs):
    if not all_pairs:
        all_pairs = []
    if pair:
        for p in pair:
            if all_pairs and p in list(all_pairs):
                continue
            all_pairs.append(p)
            npair = find_pair(p)
            return find_and_check_all(npair, all_pairs)
    else:
        return all_pairs

print(circuits)

# cncto = connector; cncts = connections
for cncto, cncts in circuits.items():
    all_connections = cncts
    for cs in cncts:
        pair = find_pair(cs)
        all_connections = find_and_check_all(pair, all_connections)
    print(cncto, all_connections)