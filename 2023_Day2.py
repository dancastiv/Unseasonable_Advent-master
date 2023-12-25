

data = []
games = []
with open('2023_Day2_games.txt') as file:
    for line in file:
        line = line.strip()
        data.append(line)
for i in data:
    temp = i.replace(': ', '; ')
    games.append(temp.split('; '))

#12 red, 13 green, 14 blue
for game in games:
    num = ''
    for letter in game[0]:
        if letter.isdigit():
            num = num + letter
        game[0] = num

class Game:
    def __init__(self, game_id, pull_1, pull_2, pull_3)
    self.game = games[0][0]

print(games)

#divide into sub lists. list name is game ID, and each sublist is the chunks divided by semicolons DONE
# for each sublist check if it works (so like check if [each colour] IN each elemend in sublist,
# and if it exists check that it's less than whatever it is the elf said).
#actuALLY HEY wouldn't a dictionary sort of work for this 
# actually just try to use objects