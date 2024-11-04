import random
import time
instructions = '''Game Rules
                    1. Rock beats Scissors (rock crushes scissors).
                    2. Scissors beat Paper (scissors cut paper).
                    3. Paper beats Rock (paper covers rock).
                    4. If both players choose the same option, it’s a tie, and you play again.
                    5. There are only 3 attempts.'''
Options = ['Rock','Paper','Scissors']
print("Let's play ROCK,PAPER and SCISSORS")
time.sleep(2)

user_id = input("Enter your username: ")
if user_id == '':
    raise NameError("USERNAME REQUIRED")
aurai = f'Hello {user_id.upper()}, Nice to meet you. I am AURAI your rival.'
print(aurai) 
time.sleep(1)
a_score = 0
u_score = 0


aurai_talk = input("What you want to do? PLAY or Go to Instructions\n")
if aurai_talk.upper()== 'PLAY':
    print("Let's Start")
else:
    print(instructions)

#Game starts

# Play the game for 3 attempts
for attempt in range(1, 4):
    print(f"\nAttempt {attempt}:")
    
    user_choice = input("What do you want to choose, Rock,Paper or Scissors\n")
    aurai_choice = random.choice(Options)
    print('USER:',user_choice) 
    print('AI:',aurai_choice)   

    if user_choice == 'Rock' and aurai_choice == 'Paper':
        print("Paper covers rock")
        a_score += 1
    elif user_choice == 'Rock' and aurai_choice == 'Scissors':
        print("Rock crushes Scissors")
        u_score += 1
    elif user_choice == 'Paper' and aurai_choice == 'Rock':
        print("Paper covers rock")
        u_score += 1
    elif user_choice== 'Paper' and aurai_choice == 'Scissors':
        print("Scissors cut paper")
        a_score += 1
    elif user_choice == 'Scissors' and aurai_choice == 'Paper':
        print("Scissors cut paper")
        u_score += 1 
    elif user_choice == 'Scissors' and aurai_choice == 'Rock':
        a_score += 1
    elif user_choice == aurai_choice:
        print("It's a tie!")
    else:
        print("You can only choose ROCK,PAPER and SCISSORS")

if u_score > a_score:
    print("You won the game! Your score is", u_score)
elif u_score == a_score:
    print("It's a tie :| Total score is", u_score)
else:
    print("Aurai won the game! Aurai score is", a_score)

print("ThankYou for playing")







































