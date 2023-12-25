def competition(guide):
    # add 1 for rock, 2 for paper, 3 for scissors
    # add 6 for a win, 3 for a draw, 0 for a loss
    score = 0
    for game in guide:
        match game:
            case 'A X': # rock v rock
                score += 4
            case 'A Y': # rock v paper
                score += 8
            case 'A Z': # rock v scissors
                score += 3
            case 'B X': # paper v rock
                score += 1
            case 'B Y': # paper v paper
                score += 5
            case 'B Z': # paper v scissors
                score += 9
            case 'C X': # scissors v rock
                score += 7
            case 'C Y': # scissors v paper
                score += 2
            case 'C Z': # scissors v scissors
                score += 6
    return score

def competition_reloaded(guide):
    # add 1 for rock, 2 for paper, 3 for scissors
    # add 6 for a win, 3 for a draw, 0 for a loss
    score = 0
    for game in guide:
        match game:
            case 'A X': # lose - rock v scissors
                score += 3
            case 'A Y': # draw - rock v rock
                score += 4
            case 'A Z': # win - rock v paper
                score += 8
            case 'B X': # lose - paper v rock
                score += 1
            case 'B Y': # draw - paper v paper
                score += 5
            case 'B Z': # win - paper v scissors
                score += 9
            case 'C X': # lose - scissors v paper
                score += 2
            case 'C Y': # draw - scissors v scissors
                score += 6
            case 'C Z': # win - scissors v rock
                score += 7
    return score


    return

guide = []
with open('2022_Day2_elf_guide.txt') as file:
    for line in file:
        line = line.strip()
        guide.append(line)
score1 = competition(guide)
score2 = competition_reloaded(guide)

print(f'Following the initial guide, the score would be: {score1}')
print(f'However, if the actual guide is followed, the score would be: {score2}')