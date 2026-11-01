with open('data_small.txt') as data:
    data = data.read().split('\n')
    sdata = []
    for d in data:
        if not d:
            continue
        sdata.append([int(d) for d in d.split(',')])
        
connections = []

cords_to_idx = {}
idx = 0
for d in sdata:
	cords_to_idx[tuple(d)] = idx
	idx += 1

def get_3d_distance(p, q):
    return (abs(p[0] - q[0]) ** 2 + abs(p[1] - q[1]) ** 2 + abs(p[2] - q[2]) ** 2) ** 0.5

#print(sdata)
for pidx, p in enumerate(sdata):
    for qidx in range(pidx + 1, len(sdata)):
    		q = sdata[qidx]
    		distance = get_3d_distance(p, q)
    		connections.append([cords_to_idx[tuple(p)], cords_to_idx[tuple(q)], distance])
           

connections = sorted(connections, key=lambda a: a[2])[0:20]

print(connections)


	
#print(cords_to_idx)

parents = [n for n in range(0, len(sdata))]
ranks = [0 for n in range(0, len(parents))]

def find(child):
    if parents[child] != child:
        parents[child] = find(parents[child])  # Path Compression
    return parents[child]
	
def union(x,y):
	xw = find(x)
	yw = find(y)
	xr = ranks[xw]
	yr = ranks[yw]
	
	if xw == yw:
		return
	
	if xr == yr:
		parents[xw] = yw
		ranks[yw] += 1
	elif xr < yr:
		parents[xw] = yw
	elif xr > yr:
		parents[yw] = xw

count = 0
for c, ct, i in connections:
	union(c, ct)
	print(f'vereine {c, ct}')
	count += 1

print(parents)
	
from collections import defaultdict

groups = defaultdict(list)

for i in range(0, len(sdata)):
	groups[find(i)].append(i)
	
groups = list(groups.values())

def lenFunk(list):
    return len(list)

groups.sort(reverse=True, key=lenFunk)

largest = []
for e in groups:
    if len(e) in largest:
        continue
    
    largest.append(len(e))
    
import math

print(largest[0:3])

print(math.prod(largest[0:3]))
		
print(groups)
