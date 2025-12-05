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
    all_highest = []
    numbers = bank
    for min in range(11, -1, -1):
        numbers, highest = find_biggest_first_with_min_numbers_after(numbers, min)
        all_highest.append(highest)
    string = ''
    for s in all_highest:
        string += str(s)
    return string

def find_biggest_first_with_min_numbers_after(numbers, min_numbers_after):
    biggest_number = 0
    biggest_number_index = 0
    for index, n in enumerate(numbers):
        if biggest_number < int(n) and len(numbers) - (index + 1) >= min_numbers_after:
            biggest_number = int(n)
            biggest_number_index = index
    return numbers[biggest_number_index + 1:], biggest_number


with open('./data/banks.txt') as file:
    total = 0
    for bank in file:
        voltage = find_two_highest2(bank.strip())
        print(voltage)
        total += int(voltage)
    print(total)
