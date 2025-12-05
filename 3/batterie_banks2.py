def find_two_highest(bank):
    highest = 0
    highest_index = 0
    for index, b in enumerate(bank):  # umgekehrte Reihenfolge
        if int(b) > highest and len(bank) - (index + 1) >= 12:
            highest = int(b)
            highest_index = index

    following_highest = []
    for z in bank[highest_index + 1:]:
        if len(following_highest) < 11:
            following_highest.append(z)
        else:
            for i, hz in enumerate(following_highest):
                if z >= hz:  # es ist auf jeden Fall größer als irgendeines
                    smallest = 9
                    smallest_index = 0
                    for i2, hz2 in enumerate(following_highest):  # suche nach dem ersten kleinsten
                        if int(hz2) < smallest:
                            smallest_index = i2
                            smallest = int(hz2)
                    del following_highest[smallest_index]
                    following_highest.append(z)
                    break

    string = str(highest)
    for s in following_highest:
        string += s
    return string

def find_two_highest2(bank):
    highest = [int(bank[0])]
    for index, b in enumerate(bank[1:]):
        for i, h in enumerate(highest):
            if int(b) > int(h):
                if len(bank) - (index + 1) >= 11:
                    for k in highest[:i]:
                        is_true = False
                        if int(k) <= int(b):
                            highest[-1] = int(b)
                            is_true = True
                            break
                    if not is_true:
                        del highest[:i]

                    break
                highest[-1] = int(b)
                break
        if len(highest) < 12:
            highest.append(int(b))
            continue
    string = ''
    for s in highest:
        string += str(s)
    return string


with open('./data/banks.txt') as file:
    total = 0
    for bank in file:
        voltage = find_two_highest2(bank.strip())
        print(voltage)
        total += int(voltage)
    print(total)
