data = []

with open('data.txt') as file:
  for line in file:
    stripped = line.strip().split(',')
    data.append([int(stripped[0]), int(stripped[1])])

sizes = []

def calc_size(first, sec):
  return (abs(first[0] - sec[0]) + 1) * (abs(first[1] - sec[1]) + 1)

for i, d in enumerate(data):
  for ii in range(i + 1, len(data)):
    dd = data[ii]
    sizes.append(calc_size(d,dd))
    
sizes = sorted(sizes, reverse=True)
print(sizes[0])
