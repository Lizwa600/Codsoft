import random
winner = {"Rock" :"Scissors", "Scissors" :"Paper", "Paper" :"Rock"}
choose_from = list(winner.keys())
computer = random.choice(choose_from)
print(computer)
user = input("Enter your choice between Rock, Paper and scissors: ")
counter_computer = 0
counter_user = 0

def handle_user_input():
    while True:
        user_input = input(f"Please eneter your choice from {choose_from}: ")
        user_in = user_input.capitalize()
        if user_in in choose_from:
            return user_in
    

# def handle_user_input(user):

#     if user not in choose_from:
#         print("Invalid input!")
#         user = input(f"Enter your choice between {choose_from} ")    
  
        
def play_game():
    if user in computer[winner]:
        counter_computer += 1
        print(f"computer won with {computer} !!!")
        
    elif computer in user[winner]:
        counter_user += 1
        print(f"you won with {user}!!!") 
        
    elif  user == computer:
        counter_computer += 1
        counter_user += 1
        print(f"you both picked{computer} so it's a draw!!!")  
    else:
        print("no winner! play again!!!")   
          
        
def determine_winner(counter_computer,counter_user):
    if counter_computer > counter_user:
        print(f"computer won with {counter_computer}, and user lost with{counter_user}")
    elif counter_user > counter_computer :
          print(f"user won with {counter_user}, and computer lost with{counter_computer}")      
    elif counter_computer == counter_user:
        print(f"It's a draw with {counter_user}")      
        

def main():
    
    user_hand = handle_user_input()
    print(user_hand)
    
    
main()