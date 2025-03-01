import random

def play():
    user = input("Choose Rock Paper or Scissors Babe! 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie baby, try again'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'Yay, You won Baby!'
    
    return 'You lost Baby!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True
    
print (play())