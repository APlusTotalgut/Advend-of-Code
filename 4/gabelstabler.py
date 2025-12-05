new_data = {}
data = {}

def check_neighbors(row, col, max_neighbors):
    row_changes = [ 1,  0, -1,-1, 1, 1, 0, -1]
    col_changes = [-1, -1, -1, 0, 0, 1, 1, 1]

    neighbors = 0

    for i in range(0, 8):
        check_row = row + row_changes[i]
        check_col = col + col_changes[i]
        if is_in_data(check_row, check_col) and data[check_row][check_col] == True:
            neighbors += 1

    return neighbors <= max_neighbors

def is_in_data(first_key, second_key):
    if first_key in data and second_key in data[first_key]:
        return True
    return False

with open('./data/rollen.txt') as file:
    for row, line in enumerate(file):
        for collum, rolle in enumerate(line.strip()):
            if not row in data:
                data[row] = {}
            data[row][collum] = rolle == '@'

hinkomm_data = {}
hinkommen_count_all = 0
hinkommen_count = None

while hinkommen_count != 0:
    hinkommen_count = 0
    for row in data:
        for col_index, col in data[row].items():
            hinkommen = False
            if col:
                hinkommen = check_neighbors(row, col_index, 3)
                if hinkommen:
                    hinkommen_count += 1
            if not row in hinkomm_data:
                hinkomm_data[row] = {}
            if not row in new_data:
                new_data[row] = {}
            hinkomm_data[row][col_index] = 'X' if hinkommen else ( '@' if col else '.')
            new_data[row][col_index] = False if hinkommen else ( True if col else False)
    data = new_data
    new_data = {}
    hinkommen_count_all += hinkommen_count

print(hinkommen_count_all)

string = ''
for row in hinkomm_data:
    for col in hinkomm_data[row].values():
        string += str(col)
    string += "\n"
print(string)

