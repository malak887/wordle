def right_pos(word, encrypted):
    correct = [0, 0, 0, 0, 0]
    for i in range(5):
        if word[i] == encrypted[i]:
            correct[i] = 1
    return correct


def letter_found(word, encrypted):
    found = [0, 0, 0, 0, 0]
    for i in range(5):
        # BUG FIX: Only check if NOT in the correct position
        if word[i] != encrypted[i]:
            if encrypted.find(word[i]) > -1:
                found[i] = 1
    return found


def validate_input(attempt, valid_words):
    if not attempt:
        return False, "Input cannot be empty. Please enter a word.", None
    
    attempt = attempt.lower().strip()
    
    if len(attempt) != 5:
        return False, f"Word must be exactly 5 letters. You entered {len(attempt)}.", None
    
    if not attempt.isalpha():
        return False, "Word must contain only letters (no numbers or special characters).", None
    
    return True, "", attempt