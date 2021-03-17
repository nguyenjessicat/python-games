import random
def game():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])
    # r>s, s>p, p>r
    if user == computer:
        return "It's a tie"
    if is_win (user, computer):
        return "You won"
    return "You lost"

    #this function below defines the rules of the game, return true if player wins
def is_win (player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'S' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print (game())
