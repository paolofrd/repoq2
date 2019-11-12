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