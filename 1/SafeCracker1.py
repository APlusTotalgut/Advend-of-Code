with open("./data/instructions.txt") as f:
    current = 50
    zeroCount = 0
    for line in f:
        direction = line[0]
        number = int(line[1:])
        faktor = number // 100
        #print(f"{number} - 100 * {faktor} == {number - 100 * faktor}")
        rest = number - 100 * faktor

        zahl = 0
        if direction == 'L':
            zahl = current - rest
            if zahl < 0:
                zahl = 99 + zahl + 1 # wegen der null ebenfalls
        elif direction == 'R':
            zahl = current + rest
            if zahl > 99:
                zahl = zahl - 99 - 1  # minus 1 because wenn counting up first digit is 0
        else:
            print('error wrong file type')
            break

        print(f"form {current} going {line} = {zahl}")
        current = zahl
        if current == 0:
            zeroCount += 1
    print(f"zero count: {zeroCount}")