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

oldtime = 1
for idx, d in enumerate(data.copy()):
    if not idx + 1 in data: continue
    print(f"{idx + 1} / {len(data) - 1}")
    start = time.time()
    for value, count in splitters.copy().items():
        for _ in range(count):
            if data[idx + 1][value] == '^':
                splitters[value + 1] += 1
                splitters[value] -= 1
                splitters[value - 1] += 1
                # print(splitters)
                splittCount += 1
                # print(splittCount)
    time_beetween = time.time() - start
    print(f'took {time_beetween}s')
    increasement = round(time_beetween / oldtime * 100)
    oldtime = time_beetween or 1
    print(f'changed about {increasement}%')
print(splittCount)