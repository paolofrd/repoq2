def isWordGuessed (secretWord, lettersGuessed):
    secret = list(secretWord)
    result = all(x in lettersGuessed for x in secret)
    if result:
        return True
    else:
        return False
    
        
def getGuessedWord (secretWord, lettersGuessed):
    lst = []
    guessword = ("a")
    for x in secretWord:
        lst = [x if x in lettersGuessed else "_" for x in secretWord]
    guessword = ''.join(lst)
    print (guessword)
    
def getAvailableLetters (lettersGuessed):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alph = []
    for x in alphabet:
        alph = ["" if x in lettersGuessed else x for x in alphabet]
        
    print (''.join(alph))
    
def Hangaroo (secretWord):
    mistakesMade = 1
    print ("Welcome to Hangaroo, user!")
    print ("Guess the word")
    while mistakesMade > 0:
        letters = input("Please guess the secret word or at least the letters that make up the secret word!: ")
        letters = letters.lower()
        lettersGuessed = list(letters)
        if isWordGuessed(secretWord,lettersGuessed) is True:
            print ("Congratulations! You guessed the correct word!")
            print ("")
            print ("Secret Word: ", secretWord)
            mistakesMade = 0
            break
        elif isWordGuessed(secretWord,lettersGuessed) is False:
            print ("Mistakes Made: ", mistakesMade)
            mistakesMade += 1
            print ("")
            print ("Guess status: ")
            getGuessedWord(secretWord, lettersGuessed)
            print ("")
            print ("Available Letters: ")
            getAvailableLetters (lettersGuessed)