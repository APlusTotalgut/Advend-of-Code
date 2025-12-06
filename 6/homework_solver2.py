import math

with open('data/homework.txt') as file:
    total = 0

    homework_clean = []
    homework = []
    for line in file:
        # print(len(line.strip().split(' ')))
        homework.append(list(line.strip('\n')))
        homework_clean.append(list(filter(lambda x: x != '', line.strip().split(' '))))

        # print(line.strip('\n').split(' '))
    print(homework)
    unclean_count = 0
    for i in range(0, len(homework_clean[0])):
        homework_size = max(len(homework_clean[0][i]), len(homework_clean[1][i]), len(homework_clean[2][i]),
                                 len(homework_clean[3][i]))
        temp_numbers = []
        for r in range(unclean_count, unclean_count + homework_size):
            temp_numbers.append(int("".join([homework[0][r] if homework[0][r] != ' ' else '',
                          homework[1][r] if homework[1][r] != ' ' else '',
                          homework[2][r] if homework[2][r] != ' ' else '',
                          homework[3][r] if homework[3][r] != ' ' else ''])))
        unclean_count = unclean_count + homework_size + 1  # plus 1 for the space between to skip that
        print(temp_numbers)
        if homework_clean[4][i] == '+':
            total += sum(temp_numbers)
        else:
            total += math.prod(temp_numbers)

    print(total)