import string

def half(item):
    chunks = len(item)
    chunk_size = len(item)//2
    halves = [item[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    return halves

def find_total(repeats):
    total = 0
    for letter in repeats:
        total = total + priorities[letter]
    return total




rucksacks = []
compartments = []
repeats = []

with open('2022_Day3_rucksacks.txt') as file:
    for line in file:
        line = line.strip()
        rucksacks.append(line)
for item in rucksacks:
    compartments.append(half(item))

for item in compartments:
    for i in list(set(item[0])&set(item[1])):
        repeats.append(i)

priorities_backwards = dict(enumerate(string.ascii_letters, 1))     
priorities = {v: k for k, v in priorities_backwards.items()}

total = find_total(repeats)

team_repeats = []
groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
for item in groups:
    for i in list(set(item[0])&set(item[1])&set(item[2])):
        team_repeats.append(i)

team_total = find_total(team_repeats)

print(f"The total of the sum of the priorities of all repeat items is: {total}.")
print(f"And the total priorities for the badges is: {team_total}.")