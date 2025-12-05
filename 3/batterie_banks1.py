def find_two_highest(bank):
    highest = 0
    second_highest = 0
    highest_index = 0
    for index, b in enumerate(bank):
        if int(b) > highest:
            second_highest = highest
            highest = int(b)
            highest_index = index
        elif int(b) > second_highest:
            second_highest = int(b)

    if highest_index == len(bank) - 1:
        return str(second_highest) + str(highest)
    else:
        second_highest = 0
        for z in bank[highest_index + 1:]:
            if int(z) > second_highest:
                second_highest = int(z)
        return str(highest) + str(second_highest)




with open('./data/banks.txt') as file:
    total = 0
    for bank in file:
        voltage = find_two_highest(bank.strip())
        print(voltage)
        total += int(voltage)
    print(total)

