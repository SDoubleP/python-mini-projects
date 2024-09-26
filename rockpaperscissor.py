import random

def play():
    user = input(" Please Choose? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It \'s a tie'
    
    if isWin(user,computer):
        return 'You Won!'
    

    return'You Lost!'




def isWin(player,opponent):
    if(player=='s'and opponent=='p')or(player=='r'and opponent=='s') \
        or (player =='p' and opponent=='r'):
        return True


print(play())