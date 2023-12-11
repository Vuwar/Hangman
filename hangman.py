import random
import time

hangman_pics= ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

words = 'bilirem yox herhalda olabilsin opsiyonel monitor divar qapi universitet seminar'.split()
remainedHearts = 0

missedLetters = ''
correctLetters = ''
gameIsDone = False

def getRandomWord(words):
    wordIndex = random.randint(0,len(words)-1)
    
    return words[wordIndex]

def displayBoard(missedLetters, correctLetters, trueWord):
    print(hangman_pics[len(missedLetters)])
    print()
    
    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()
    
    blanks = "_" * len(trueWord)
    
    for x in range(len(trueWord)):
        if trueWord[x] in correctLetters:
            blanks = blanks[:x] + trueWord[x] + blanks[x+1:]
    
    for letter in blanks:
        print(letter, end='')

def getGuess(alreadyGuessed):
    while True:
        print()
        print('Guess a letter.')
        
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
    
def playAgain():
    print('Do you want to play again? (yes/no)')
    return input().lower().startswith('yes')

trueWord = getRandomWord(words)

while True:
    displayBoard(missedLetters, correctLetters, trueWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in trueWord:
        correctLetters = correctLetters + guess
        
        foundAllLetters = True
        for i in range(len(trueWord)):
            if trueWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is "' + trueWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hangman_pics) - 1:
            displayBoard(missedLetters, correctLetters, trueWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + trueWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            trueWord = getRandomWord(words)
        else:
            break