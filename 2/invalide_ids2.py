def has_same_sequence(number):
    str_number = str(number)
    length = len(str_number)
    for i in range(2, length + 1):
        if length % i != 0:
            continue
        teiler = int(length / i)
        parts = []
        for p in range(0, length, teiler):
            parts.append(str_number[p:p+teiler])
        is_all_same = True
        for p in range(1, len(parts)):
            if (parts[p] != parts[p - 1]):
                is_all_same = False
                break
        if is_all_same:
            return True
    return False

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



