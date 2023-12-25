def aim_and_move(data):
    forward = 0
    aim = 0
    depth = 0
    for i in data:
        if i[0] == 'f':
            forward += int(i.lstrip('forward '))
            depth += aim * int(i.lstrip('forward '))
        elif i[0] == 'd':
            aim += int(i.lstrip('down '))
        elif i[0] == 'u':
            aim -= int(i.lstrip('up '))
    position = forward * depth
    return position



    
data = []
forward = []
down = []
up = []
with open('2021_Day2_instructions.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)
for i in data:
    if i[0] == 'f':
        forward.append(int(i.lstrip('forward ')))
    elif i[0] == 'd':
        down.append(int(i.lstrip('down ')))
    elif i[0] == 'u':
        up.append(int(i.lstrip('up ')))

horizontal = sum(forward)
depth = sum(down) - sum(up)

position = aim_and_move(data)
print(f"A horizontal length of {horizontal} times a depth of {depth} is equal to {horizontal * depth}.")
print(f"Following the right instructions, the final result is instead {position}.")