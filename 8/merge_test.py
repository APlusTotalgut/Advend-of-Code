circuits = test_liste = [
    [1, 2],        # Überschneidungskette A-B-C
    [2, 3],
    [3, 4],
    [5, 6],        # zweite Kette D-E
    [6, 7],
    [8, 9],        # isolierte Gruppe
    [10, 11],      # Überschneidung mit mehrfacher Überschneidung
    [11, 12],
    [10, 12],      # gleiche Zahlen wie vorher, um Mehrfachzählung zu testen
    [13, 14],      # separate kleine Gruppe
    [14, 15],
    [4, 1]         # verbindet Cluster 1 (1,2,3,4) über eine andere Reihenfolge
]

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
					print(circuits, '\n')
					print(f"merging \n{c} \nand\n{inc}\n")
					circuits[i] = merge_lists(c, inc)
					del circuits[idx]
					check_for_merging(i, circuits[i])
#print(circuits)
for i, c in enumerate(circuits):
    check_for_merging(i,c)
            
right_endresult = [
    [1, 2, 3, 4],
    [5, 6, 7],
    [8, 9],
    [10, 11, 12],
    [13, 14, 15]
]
if circuits == right_endresult:
		print('test succed')
else:
		print(circuits, "\n")
		print('is not', '\n')
		print(right_endresult)


