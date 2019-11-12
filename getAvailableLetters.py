def getAvailableLetters (lettersGuessed):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alph = []
    for x in alphabet:
        alph = ["" if x in lettersGuessed else x for x in alphabet]
        
    print (''.join(alph))