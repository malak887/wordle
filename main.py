
from encrypted_word import *
from check import*
from colour import*
encrypted=get_word()

print("quess the word and win !!")
print("you have 6 attempts")

flag=False
for k in range(6):
    attempt = input()
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
    

if flag==False:
   print("you lose")
   print("6/6 wrong attempts")
   print("the encypted word was ",encrypted)
   
        
    




 