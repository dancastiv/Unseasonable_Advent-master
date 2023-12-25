
def addition(data):
    digits = ''
    numbers = []
    for i in data:
        if i.isalpha():
            pass
        else:
            for letter in i:
                if letter.isnumeric():
                    digits += letter
            numbers.append(digits[0] + digits[-1])
            digits = ''
        numbers = list(map(int, numbers))
    return sum(numbers)
    
def addition_reloaded(data):
    digits = ''
    converted = []
    numbers = []
    for i in data:
        temp = ''
        x = 0
        while x < len(i):
            if 'one' in i[x:x+3]:
                temp = temp + '1'
            if 'two' in i[x:x+3]:
                temp = temp + '2'
            if 'three' in i[x:x+5]:
                temp = temp + '3'
            if 'four' in i[x:x+4]:
                temp = temp + '4'
            if 'five' in i[x:x+4]:
                temp = temp + '5'
            if 'six' in i[x:x+3]:
                temp = temp + '6'
            if 'seven' in i[x:x+5]:
                temp = temp + '7'
            if 'eight' in i[x:x+5]:
                temp = temp + '8'
            if 'nine' in i[x:x+4]:
                temp = temp + '9'
            else:
                temp = temp + i[x]
            x += 1
        converted.append(temp)  
    for i in converted:
        if i.isalpha():
            pass
        else:
            for letter in i:
                if letter.isnumeric():
                    digits += letter
            numbers.append(digits[0] + digits[-1])
            digits = ''
        numbers = list(map(int, numbers))
    return sum(numbers)


data = []
with open('2023_Day1_calibration.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)

sum1 = addition(data) 
#had to change the name from sum because it confused the computer when I tried to sum in addition_reloaded and got int object not callable. 
# lol TIL
sum_reloaded = addition_reloaded(data)

print(f"The answer to the first part is: {sum1}")
print(f"The answer to the second part is: {sum_reloaded}")