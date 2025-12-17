import time

with open('./data.txt') as file:
    data = {}

    for idx, l in enumerate(file):
        middle = int(len(l.strip()) / 2)
        for index, c in enumerate(l.strip()):
            if idx not in data:
                data[idx] = {}
            data[idx][index] = c


from collections import Counter
splitters = Counter()
splitters[middle] += 1
splittCount = 1

for idx, d in enumerate(data.copy()):
    if not idx + 1 in data: continue
    start = time.time()
    for value, count in splitters.copy().items():
        if data[idx + 1][value] == '^':
            splitters[value + 1] += count
            splitters[value] -= count
            splitters[value - 1] += count

            splittCount += count

print(splittCount)