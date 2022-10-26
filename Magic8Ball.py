import random
import sys

messages = ['It is certain', 'Definitely so', 'Yes', 'Reply is Hazy, try again', 'Ask again later', 'No', 'Outlook not good',
            'Very doubtful', 'I do not think so', 'I do not believe you should,' 'Tempting... but no', 'Go for it!',
            'Do not ask Magic 8 Ball such nonsense', 'I disagree', 'Maybe', 'A different time', 'Seriously?',
            'Do or do not, there is no try',
            'Take a chance', 'Do not']

while True:
    print('\nDo you have a question for Magic 8 Ball? \nPress st to stop \n')
    playerQuestion = str(input())
    if playerQuestion == 'st':
        print("May Magic 8 Ball guide you")
        sys.exit()
    else:
        print(messages[random.randint(0, len(messages) - 1)])