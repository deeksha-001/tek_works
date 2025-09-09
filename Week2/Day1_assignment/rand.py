import random
def rps():
    l = ['rock', 'paper', 'scissors']
    user = input("Enter your choice (rock/paper/scissors): ").lower()
    comp = random.choice(l)
    print("Computer chose:", comp)
    if user == comp:
        return "It's a tie!"
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
    
print(rps())