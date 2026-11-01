data = []

print('start')
def check_direction(start, end):
    if start > end:
        return 1
    elif start < end:
        return -1
    return 1


with open('data_small.txt') as file:
    for line in file:
        stripped = line.strip().split(',')
        data.append([int(stripped[0]), int(stripped[1])])

sizes = []

print('data is da')
from collections import defaultdict

cdict = defaultdict(lambda: defaultdict(list))
biggest = [0, 0]
for i, d in enumerate(data):
    if i < len(data) - 1:
        next_item = i + 1
    else:
        next_item = 0

    connection = data[next_item]
    #print(d)
    direction = check_direction(connection[0], d[0])

    for x in range(d[0], connection[0] + direction, direction):

        direction = check_direction(connection[1], d[1])

        for y in range(d[1], connection[1] + direction, direction):
            #print(x, y)
            if biggest[0] < x:
                biggest[0] = x
            if biggest[1] < y:
                biggest[1] = y
            cdict[y][x] = 1

cdict_x_first = defaultdict(lambda: defaultdict(list))
biggest = [0, 0]
for i, d in enumerate(data):
    if i < len(data) - 1:
        next_item = i + 1
    else:
        next_item = 0

    connection = data[next_item]
    #print(d)
    direction = check_direction(connection[0], d[0])

    for x in range(d[0], connection[0] + direction, direction):

        direction = check_direction(connection[1], d[1])

        for y in range(d[1], connection[1] + direction, direction):
            #print(x, y)
            if biggest[0] < x:
                biggest[0] = x
            if biggest[1] < y:
                biggest[1] = y
            cdict_x_first[x][y] = 1
#print(biggest)
for d in data:
    cdict[d[1]][d[0]] = 0

for d in data:
    cdict_x_first[d[0]][d[1]] = 0

print('cdict mid finished')

print(cdict_x_first)
print(cdict)

#for y, iy in cdict.items():
#    print(iy)
#    start = list(iy.items())[0][0]
#    end = list(iy.items())[-1][0]
#    direction = check_direction(end, start)
#    print(start, end, direction)
#    for x in range(start, end, direction):
#        #print(x, y)
 #       if cdict[y][x] != 0 and cdict[y][x] != 1:
#            cdict[y][x] = 1
print('cdict is da')
print(cdict)

for y in range(0, biggest[1] + 1):
    for x in range(0, biggest[0] + 1):
        val = cdict[y].get(x, None)  # None, falls Key nicht existiert
        if val == 1:
            #print('X', end="")
            pass
        elif val == 0:
            #print("#", end="")
            pass
        else:
            #print(".", end="")
            pass
    #print("")
print(cdict)


def calc_size(first, sec):
    return (abs(first[0] - sec[0]) + 1) * (abs(first[1] - sec[1]) + 1)

#print(data)
#print(cdict)
def check_given_range(rstart, rend, steady_letter):
    direction = check_direction(rend, rstart)
    for r in range(rstart, rend + direction, direction):
        if steady_letter[0] == 'x':
            s = cdict[r].get(steady_letter[1], None)
            print(r, steady_letter[1], s)
            if s != 1 and s != 0:
                print('')
                # y verändert sich nach unten -> Zahl wird größer
                if direction == 1 and max(cdict_x_first[steady_letter[1]].keys()) > rend:
                    break
                elif direction == -1 and min(cdict_x_first[steady_letter[1]].keys()) < rend:
                    break
                return False
            #print(r, steady_letter[1], s)
        else:
            s = cdict[steady_letter[1]].get(r, None)
            print(r, steady_letter[1], s)
            if s != 1 and s != 0:
                if direction == 1 and max(cdict[steady_letter[1]].keys()) > rend:
                    break
                elif direction == -1 and min(cdict[steady_letter[1]].keys()) < rend:
                    break
                return False
            #print(steady_letter[1],r, s)

    return True


for i, d in enumerate(data):
    for ii in range(i + 1, len(data)):
        dd = data[ii]
        #print('checking: ')
        #print(d)
        #print(dd)
        #print('now check_given_range')
        if (check_given_range(d[1], dd[1], ['x', d[0]]) and
                check_given_range(d[0], dd[0], ['y', dd[1]]) and
                check_given_range(dd[1], d[1], ['x', dd[0]]) and
                check_given_range(d[0], dd[0], ['y', d[1]])):
            print('ja', d, dd)
            sizes.append(calc_size(d, dd))

sizes = sorted(sizes, reverse=True)
print(cdict)
print('endresult: ' + str(sizes[0]))
