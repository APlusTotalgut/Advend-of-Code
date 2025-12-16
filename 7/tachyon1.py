with open('./data.txt') as file:
    data = {}

    for idx, l in enumerate(file):
        middle = int(len(l.strip()) / 2)
        for index, c in enumerate(l.strip()):
            if idx not in data:
                data[idx] = {}
            data[idx][index] = c

    splitters = set()
    splitters.add(middle)
    splittCount = 0
    for idx, d in enumerate(data.copy()):

        for s in splitters.copy():
            if not idx + 1 in data:
                continue
            if data[idx + 1][s] == '^':
                splitters.remove(s)
                splitters.add(s + 1)
                splitters.add(s - 1)

                splittCount += 1

print(splittCount)
