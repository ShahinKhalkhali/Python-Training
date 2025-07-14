tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |
      |
      |
    ~~~~~'''

def hangman(word_length, guess_display, wrong_guesses): 
    global tree
    if wrong_guesses == 0:
        print({})

    elif wrong_guesses == 1:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 2:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |     |
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 3:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 4:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|\\
      |
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 5:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|\\
      |    /`
    ~~~~~'''
        print(tree)
    
    elif wrong_guesses == 6:
        tree = ''' 
    (```)
   (     )
    (_ _)   
      |------
      |     |
      |     O
      |    /|\\
      |    /`\\
    ~~~~~'''
        print(tree)
    
    for i in word_length:
        # Print current list
        print(f"{guess_display[i]}", end=' ')