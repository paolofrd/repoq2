def getGuessedWord (secretWord, lettersGuessed):
    lst = []
    guessword = ("a")
    for x in secretWord:
        lst = [x if x in lettersGuessed else "_" for x in secretWord]
    guessword = ''.join(lst)
    print (guessword)