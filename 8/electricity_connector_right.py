import math

def get_3d_distance(p, q):
    return (abs(p[0] - q[0]) ** 2 + abs(p[1] - q[1]) ** 2 + abs(p[2] - q[2]) ** 2) ** 0.5

with open('data_small.txt') as data:
    data = data.read().split('\n')
    sdata = []
    for d in data:
        if not d:
            continue
        sdata.append([int(d) for d in d.split(',')])

connections = {}
all_connections = []

#print(sdata)
for pidx, p in enumerate(sdata):
    lowest = []  # 0 => point itself ; 1 => distance
    for qidx, q in enumerate(sdata):
        if qidx == pidx:
            continue
        
        if [list(q), list(p)] in all_connections:
        		continue
        #if any(p in c[])
        distance = get_3d_distance(p, q)
        if not lowest or distance < lowest[1]:
            lowest = [q, distance]
            
    if lowest:
        connections[tuple(p)] = lowest
        all_connections.append([list(p), list(lowest[0])])

connections = dict(sorted(connections.items(), key=lambda a: a[1][1]))
print(connections)
#print('\n')
for i, (a, c) in enumerate(connections.items()):
		if i >= 10:
				continue
#		print(a, c[0])
#print('\n')

#print(connections)

#print(connections)

circuits = []
#geht nicht circuits ja leer
for index in range(0,10):
    cp = list(connections.items())[index][0]
    cq = list(connections.items())[index][1]
    #print('das muss mehrfach')
    #print(list(cp), cq[0])
    #print(circuits)
    #print('\n')
    if not circuits:
        circuits.append([list(cp), cq[0]])
    if not any(list(cp) in c or cq[0] in c for c in circuits):
        circuits.append([list(cp), cq[0]])
        #print('3')
        continue
    for c in circuits:
        #print(list(cp))
        #print(cq[0])
        #print('in')
        #
        #print(c)
        if (list(cp) in c) and not (cq[0] in c):
            c.append(list(cq[0]))
            #print('1')
        elif not list(cp) in c and cq[0] in c:
            c.append(list(cp))
            #print('2')
        #else:
            #print('skipping')
            
        
            
        #print(circuits)
        #print('\n')
        #print(c)
        #print('\n')

def merge_lists(first, second):
    for f in first:
        if f not in second:
            second.append(f)
    return second

def check_for_merging(i,c):
		for idx, inc in enumerate(circuits):
				if i == idx:
						continue
				if any(ck in inc for ck in c):
					#print(circuits, '\n')
					#print(f"merging \n{c} \nand\n{inc}\n")
					circuits[i] = merge_lists(c, inc)
					del circuits[idx]
					check_for_merging(i, circuits[i])
#print(circuits)
for i, c in enumerate(circuits):
    check_for_merging(i,c)
    
def lenFunk(list):
    return len(list)

circuits.sort(reverse=True, key=lenFunk)
#print(circuits)
largest = []
for e in circuits:
    if len(e) in largest:
        continue
    
    largest.append(len(e))
    
print(circuits)

# Alle Zahlen flach zusammenfügen
flat_numbers = [tuple(inner) for outer in circuits for inner in outer]
# Duplikate prüfen
from collections import Counter
counts = Counter(flat_numbers)
duplicates = [num for num, count in counts.items() if count > 1]

print(duplicates)
largest = largest[0:3]
print(largest)
print(math.prod(largest))

