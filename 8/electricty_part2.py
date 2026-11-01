with open('data.txt') as data:
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
           

big_connections = sorted(connections, key=lambda a: a[2])
connections = big_connections

#print(connections)

print('bisschen was schon geschafft')
	
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

idx_to_cords = {b: a for a, b in cords_to_idx.items()}

from collections import defaultdict

for c, ct, i in connections:
	#print(f'vereine {idx_to_cords[c], idx_to_cords[ct]}')
	union(c, ct)
	groups = defaultdict(list)

	for i in range(0, len(sdata)):
		groups[find(i)].append(i)
		
	#groups = list(groups.values())
	
	def lenFunk(list):
	    return len(list)
	
	#groups.sort(reverse=True, key=lenFunk)
	#print(groups)
	if (sorted(parents) == parents):
		print(idx_to_cords[c][0]* idx_to_cords[ct][0])
		
		break

#print(parents)
	


groups = defaultdict(list)

for i in range(0, len(sdata)):
	groups[find(i)].append(i)
	
groups = list(groups.values())

def lenFunk(list):
    return len(list)

groups.sort(reverse=True, key=lenFunk)

print('groups', groups)

#print('connections', big_connections)

#print('jetzt start von possible')

#idx_to_cords = {b: a for a, b in cords_to_idx.items()}

#possible_connectors = defaultdict(list)
#for i, g in enumerate(groups):
#	print(possible_connectors)
	
#	#for ig in g:
		
#		for inner_i in range(i + 1, len(groups)):
	#		inner_inner_g = groups[inner_i]
		#	for i_i_t in inner_inner_g:
				#print('inner_inner_g', i_i_t)
				#print('ig', ig)
			#	result = get_3d_distance(list(idx_to_cords[ig]), list(idx_to_cords[i_i_t]))
				#print('result', result)
				#possible_connectors[i].append([ig, i_i_t, result])

#print(possible_connectors)
#final_connections = []

print('jetzt final connections')

#for key in possible_connectors:
#	final_connections.append(sorted(
#		possible_connectors[key],
#		key=lambda a: a[2]
#		)[0])
		

#print(final_connections)
#print(idx_to_cords[final_connections[-1][0]], idx_to_cords[final_connections[-1][1]])
#print(idx_to_cords[final_connections[-1][0]][0] * idx_to_cords[final_connections[-1][1]][0] )

