def find_redundancy(pairs):
    first = []
    second = []
    counter = 0
    for i in pairs:
        first = list(map(int, i[0].split("-")))
        second = list(map(int, i[1].split("-")))
        if (first[0] <= second[0]) and (first[1] >= second[1]):
            counter += 1
        elif (first[0] >= second[0]) and (first[1] <= second[1]):
            counter += 1
    return counter

def find_partial_redundancy(pairs):
    first = []
    second = []
    counter = 0
    for i in pairs:
        first = list(map(int, i[0].split("-")))
        second = list(map(int, i[1].split("-")))
        if first[0] <= second[0] and first[1] >= second[0]:
            counter += 1
        elif first[0] >= second[0] and first[0] <= second[1]:
            counter += 1
    return counter


data = []
pairs = []
with open('2022_Day4_pairs.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)
for i in data:
   pairs.append(i.split(","))

counter1 = find_redundancy(pairs)
counter2 = find_partial_redundancy(pairs)


print(f"The number of fully redundant pairs is {counter1}.")
print(f"The number of partially redundant pairs is {counter2}")
