
def right_pos(word,encrypted):#if the letter is right and right posistion , will have a true in list
    
    l_right = [0,0,0,0,0]
    for i in range(5):
        if word[i]==encrypted[i]:
            l_right[i]=1
    return l_right




def letter_found(word,encrypted):#if the letter is right and wrong posistion , will have a true in list
    l_found=[0,0,0,0,0]
    for i in range(5):
        x= encrypted.find(word[i])
        if x>-1 :
            l_found[i]=1
    return l_found




def validate_input(attempt, valid_words):
    """
    Validates user input for the Wordle game.
    Returns: (is_valid, error_message, normalized_word)
    """
    # Check if input is empty
    if not attempt:
        return False, "Input cannot be empty. Please enter a word.", None
    
    # Convert to lowercase for consistency
    attempt = attempt.lower().strip()
    
    # Check length
    if len(attempt) != 5:
        return False, f"Word must be exactly 5 letters. You entered {len(attempt)}.", None
    
    # Check if only contains letters
    if not attempt.isalpha():
        return False, "Word must contain only letters (no numbers or special characters).", None
    
    return True, "", attempt
