def PossibleCombinations(A_choises, B_choises):
    for a in A_choises:
        t = ''
        for b in B_choises:
            t += f"'{a} {b}': _, "
        print(t)
f = open('input.txt')

playerA_choises = ['A', 'B', 'C'] #rock, paper, scissors
playerB_choises = {'X': 1, 'Y': 2, 'Z': 3} #rock, paper, scissors
score_rule = {'L': 0, 'D': 3, 'W': 6}

# PossibleCombinations(playerA_choises,playerB_choises.keys())
combinations = {'A X': 4, 'A Y': 8, 'A Z': 3,
                'B X': 1, 'B Y': 5, 'B Z': 9,
                'C X': 7, 'C Y': 2, 'C Z': 6}

score = 0
for l in f.readlines():
    match = l[:-1]
    score += combinations[match]
print(score) #pt1 11767

f.seek(0) #Move file's pointer position to the beginning
score_rule = {'X': 0, 'Y': 3, 'Z': 6}
combinations = {'A X': 'Z', 'A Y': 'X', 'A Z': 'Y',
                'B X': 'X', 'B Y': 'Y', 'B Z': 'Z',
                'C X': 'Y', 'C Y': 'Z', 'C Z': 'X'}
score = 0
for l in f.readlines():
    playerA_choise = l[0]
    match_outcome = l[-2] #[-1] is \n
    match = f'{playerA_choise} {match_outcome}'
    playerB_choise = combinations[match]

    score += score_rule[match_outcome] + playerB_choises[playerB_choise]
print(score) #pt2 13886

f.close()
