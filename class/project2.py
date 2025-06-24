#game rock paper scissors
from getpass import getpass
import random
def game(player1,player2):

    if player1 == player2: 
      return None    
    elif player1== 'p':
        if player2 == 'r':
            return True
        elif player2 == 's':
                return False
        
    elif player1== 's':
        if player2 == 'p':
            return True
        elif player2 == 'r':
                return False 
                       
    elif player1== 'r':
        if player2 == 'p':
            return True
        elif player2 == 's':
                return False   
        
player1=getpass(str("player1 turn:rock(r) paper(p) or scissors(s):\n"))
 

print(f"Player1 chose: {player1}")

# player2=getpass(str("player2 turn: rock(r) paper(p) or scissors(s):\n"))
# For simplicity, we will let player2 be a random choice
player2 = random.choice(['r', 'p', 's'])

print(f"Computer chose: {player2}")

a = game(player1,player2)

if a== None:
    print("The game is tie!")

elif a:# True means player1 wins
     
     print("Player1 WIN!")
else:# False means player2 wins
    print("Player2 WIN!")   
