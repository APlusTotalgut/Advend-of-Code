
def recursive(pattern, buttons, combination_list, empty_buttons):
    new_combination_list = []
    for comp in combination_list:
        for b in range(0, len(buttons)):
            empty_buttons_cp = empty_buttons.copy()
            comp_cp = comp.copy()
            comp_cp.append(b)
            new_combination_list.append(comp_cp)
            for button in comp_cp:
                for switch in buttons[button]:
                    empty_buttons_cp[switch] = not empty_buttons_cp[switch]

            if empty_buttons_cp == pattern:
                return comp_cp
            
    return recursive(pattern, buttons, new_combination_list, empty_buttons) 


with open('data.txt') as data:
    total = 0
    for l in data:
        splitted = l.split(' ')
        pattern = splitted[0].strip("[]").split()[0]
        pattern = [True if p == "#" else False for p in pattern]

        buttons = [[int(i) for i in s.strip('()').split(',')] for s in splitted[1:-1]]
        empty_buttons = [False for i in range(0, len(pattern))]
        found = 0
        combination_list = []
        for i, b in enumerate(buttons):
            empty_buttons_cp = empty_buttons.copy()
            for switch in b:
                empty_buttons_cp[switch] = not empty_buttons_cp[switch]
            if empty_buttons_cp == pattern:
                found = 1
                break
            combination_list.append([i])

        if found == 0:
            comp = recursive(pattern, buttons, combination_list, empty_buttons)
            total += len(comp)
        else:
            total += 1

    print(total)
