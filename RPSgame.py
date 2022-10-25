import random
import sys

print('*** Rock, Paper, Scissors, the Game! ***')

# variables to keep track of records
wins = 0
losses = 0
ties = 0

while True:  # the main game loop 
    print('%s WINS, %s, LOSSES %s TIES' % (wins, losses, ties))
    while True:  # player input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print("Thanks for playing!")
            sys.exit()  # Quits the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # breaks input loop
        print(' Type one of r , p, s, or q.')

    # displays what the player chooses:
    if playerMove == 'r':
        print('Rock! vs...')
    elif playerMove == 'p':
        print('Paper! vs...')
    elif playerMove == 's':
        print('Scissors! vs ....')

    # Displays what computer chose

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock!')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper!')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors!')

    # Displays record

    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('Winner!!!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Winner!!!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Winner!!!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Loss :(')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Loss :(')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Loss :(')
        losses = losses + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Loss :(')
        losses = losses + 1
