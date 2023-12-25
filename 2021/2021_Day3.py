
data = []
with open('2021_Day3_bits.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)
x = 0
gamma = ''
while x < len(data[0]):
    counter0 = 0
    counter1 = 0
    for reading in data:
        if reading[x] == '0':
            counter0 += 1
        elif reading[x] == '1':
            counter1 += 1
    if counter0 > counter1:
        gamma = gamma + '0'
    else:
        gamma = gamma + '1'
    x += 1
epsilon = ''
for i in gamma:
    if i == '0':
        epsilon += '1'
    else:
        epsilon += '0'

consumption = int(gamma, 2) * int(epsilon, 2)


print(consumption)