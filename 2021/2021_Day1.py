
depths = []
with open('2021_Day1_depths.txt') as file:
    for line in file:
        line = line.strip()
        depths.append(line)
depths = list(map(int, depths)) #there are edge cases lead to wrong answer if you don't convert to int

counter1 = 0
counter2 = 0        
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]: 
        counter1 += 1

sliding_window = [depths[i:i+3] for i in range(0, len(depths))]
sums = []
for window in sliding_window:
    sums.append(sum(window))
for i in range(1, len(sums)):
    if sums[i] > sums[i-1]:
        counter2 += 1
        
print(f"The total number of depth increases is: {counter1}.")
print(f"The total number of depth increases for the sliding windows is {counter2}.")