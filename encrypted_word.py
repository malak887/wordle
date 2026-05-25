import random
import os

# Load words from file with error handling
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    words_file = os.path.join(current_dir, "words.txt")
    
    with open(words_file, "r") as f:
        data = [line.strip().lower() for line in f if line.strip()]
    
    if not data:
        raise ValueError("words.txt is empty!")
        
except FileNotFoundError:
    print("Error: words.txt file not found!")
    data = []


def get_word():
    if not data:
        raise ValueError("No words available! Check that words.txt exists.")
    return random.choice(data)
