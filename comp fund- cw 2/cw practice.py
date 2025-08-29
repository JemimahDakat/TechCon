def guess_word():
    letterList = []
    stringword = input("please enter a word").lower()
    
    for i in range (1,5):
        letter = input("please enter a letter").lower()
        letterList.append(letter)
    if stringword == ''.join(letterList):
        print ("TRUE")
    else:
        print ("FALSE")

guess_word()