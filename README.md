
[Project name]: wordle  
[summary]: the console app saves an encrypted word of 5 letters, which the user should guess.
the user is given 6 attempts to guess , in each attempt if the word the user entered contains a letter found in the encrypted  but not in the correct position ,
then the letter will be coloured yellow , if it's in the right position it will be coloured green

[to import]:
user have to import "corolama" to run the app.

[implementation]:

First: the program goes through the dataset provided , and assign it to a list .

Second: random choose from that list , and assign it to the variable : encrypted in main

Third: when taking attempts from user , call the functions right_pos , l_found with the parameters (the user input , the encrypted ), they go check the letters in the input ,
if there's a letter found in wrong position , then save its index in a list , to be returned by the function.
if there's a letter in its right position , it's index saved in another list.
both lists are assigned to a lists in main: letter_found , right_pos

Fourth: for letters with their index in right_pos , sent as parameters in function "colouring" , to be coloured as green
and for whose index in letter found , sent as parameters to "colouring", to be coloured yellow 

Fifth: if the user guessed it right , after it all apear in green , the game is ended.
