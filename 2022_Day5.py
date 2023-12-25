

data = []
meow = []
with open('2022_Day5_instructions.txt') as file:
    crates, instructions = [
        part.split("\n") for part in file.split("\n\n")
    ]
    for line in file:
        line = line.strip()
        data.append(line)


print(meow)
print(data)
print(crates)
print(instructions)