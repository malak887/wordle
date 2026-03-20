
from encrypted_word import *
from check import*
from colour import*
encrypted=get_word().lower()

print("guess the word and win!!")
print("you have 6 attempts")

flag=False
for k in range(6):
    # Get valid input from user
    valid_input = False
    while not valid_input:
        attempt = input("Enter your guess (5 letters): ").lower()
        is_valid, error_msg, normalized_attempt = validate_input(attempt, data)
        if is_valid:
            valid_input = True
            attempt = normalized_attempt
        else:
            print(f"{error_msg}")
    
    if attempt==encrypted:flag=True
    l_right=right_pos(attempt,encrypted)
    l_found= letter_found(attempt,encrypted)
    output=""
    for x in range(5):
        if l_right[x]==1: 
         output= colouring(attempt[x],output,"green")
        elif l_found[x]==1:
         output=colouring(attempt[x],output,"yellow")
        else: output +=attempt[x] 
    print("               ",output)  
    if flag :
       print("correct guess")
       print("you won")
       break
    else:
        print(f"Attempt {k+1}/6")
    

if flag==False:
   print("you lose")
   print("6/6 wrong attempts")
   print("the encrypted word was: ",encrypted)
   
        
    




 