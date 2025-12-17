# Task:
# It's now just one beam which is considered as quantum beam, that means it basically splits up every time it hits an
# obstacle each of them is considered as timeline but once a beam hits an obstacle it's not dead it just takes both
# paths.

# Goal:
# find all the timelines. To take it exact GOAL is just to find out how many timelines there are

# Approach:
# I start of with the S beam at ´middle´ and going to take every turn left. For the right I call the function again to
# follow that specific path: RECURSION
# In the function first of all time_line_count will be increased

with open('./data.txt') as file:
    data = {}

    for idx, l in enumerate(file):
        middle = int(len(l.strip()) / 2)
        for index, c in enumerate(l.strip()):
            if idx not in data:
                data[idx] = {}
            data[idx][index] = c
    #print(data)


time_line_count = 0


def follow_time_line(row, column):
    #print(str(row) + " of " + str(len(data)))
    global time_line_count
    #print(time_line_count)
    time_line_count += 1
    for r in range(row, len(data) + 1):
        if not r + 1 in data:
            continue
        if data[r + 1][column] == '^':
            # a new timeline begins at the right
            follow_time_line(r + 2, column + 1)
            column -= 1


import time
start = time.time()

follow_time_line(1, middle)

end = time.time()

print(time_line_count)
print("Dauer:", end - start, "Sekunden")