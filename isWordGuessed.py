def isWordGuessed (secretWord, lettersGuessed):
    secret = list(secretWord)
    result = all(x in lettersGuessed for x in secret)
    if result:
        return True
    else:
        return False