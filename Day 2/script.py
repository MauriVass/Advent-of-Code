def PossibleCombinations(A_choises, B_choises):
    for a in A_choises:
        t = ''
        for b in B_choises:
            t += f"'{a} {b}': _, "
        print(t)
f = open('input.txt')

playerA_choises = ['A', 'B', 'C'] #rock, paper, scissors
playerB_choises = {'X': 1, 'Y': 2, 'Z': 3}
score_rule = {'L': 0, 'D': 3, 'W': 6}

# PossibleCombinations(playerA_choises,playerB_choises.keys())
combinations = {'A X': 4, 'A Y': 8, 'A Z': 3,
                'B X': 1, 'B Y': 5, 'B Z': 9,
                'C X': 7, 'C Y': 2, 'C Z': 6}

score = 0
for l in f.readlines():
    match = l[:-1]
    score += combinations[match]
print(score)
