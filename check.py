l_right=[0,0,0,0,0]
def right_pos(word,encrypted):#if the letter is right and right posistion , will have a true in list
    for i in range(5):
        if word[i]==encrypted[i]:
            l_right[i]=1
    return l_right



l_found=[0,0,0,0,0]
def letter_found(word,encrypted):#if the letter is right and wrong posistion , will have a true in list
    for i in range(5):
        x= encrypted.find(word[i])
        if x>-1  and l_right[i]==0:
            l_found[i]=1
    return l_found
