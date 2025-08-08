import random
with open("words.txt", "r") as f:
    data = [line.strip() for line in f] #read the file , and save the strings in a list

def encrypted_word():
  
    return random.choice(data) #choose a random string from the list
print(encrypted_word())