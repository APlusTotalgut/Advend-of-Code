def has_same_sequence(number):
    str_number = str(number)
    length = len(str_number)
    if length % 2 != 0:
        return False
    half = int(length / 2)

    part1 = str_number[0:half]
    part2 = str_number[half:]
    if part1 == part2:
        return True


allNumbers = 0
with open('./data/ids.txt') as file:
    line = file.readline()
    sequences = line.split(',')
    for s in sequences:
        start, end = s.split('-')
        for z in range(int(start), int(end)):
            if has_same_sequence(z):
                allNumbers += z
print(allNumbers)
