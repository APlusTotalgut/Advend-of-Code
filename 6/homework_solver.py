import math

with open('data/homework_example.txt') as file:
    homework_clean = []
    homework = []
    for line in file:
        homework.append(list(filter(lambda x: x != '', line.strip().split(' '))))
    total = 0
    for i in range(0, len(homework[0])):
        if homework[4][i] == '+':
            total += sum([int(homework[0][i]), int(homework[1][i]), int(homework[2][i]), int(homework[3][i])])
        else:
            total += math.prod([int(homework[0][i]), int(homework[1][i]), int(homework[2][i]), int(homework[3][i])])

    print(total)